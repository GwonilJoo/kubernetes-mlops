from uuid import uuid4, UUID
from typing import List
import os

from src.domain.experiment import Experiment
from src.requests.experiment import ExperimentRequest, ExperimentListRequest

JOB_TEMPLATE = \
"""cat << EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: ml-epoch-%02d-lr-%.3f-bs-%03d
spec:
  template:
    spec:
      containers:
        - name: ml
          image: gwonil/ml:latest
          resources:
            requests:
              memory: "4000Mi"
          env:
            - name: LEARNING_RATE
              value: "%s"
            - name: EPOCHS
              value: "%s"
            - name: BATCH_SIZE
              value: "%s"
            - name: EXPERIMENT_ID
              value: "exp%02d"
            - name: DB_HOST
              value: "mongo"
            - name: DB_PORT
              value: "27017"
            - name: SAVE_DIR
              value: "/saved"
            - name: MNIST_DIR
              value: "/saved/MNIST_data/"
            - name: PYTHONUNBUFFERED
              value: "0"
          volumeMounts:
            - name: varlog
              mountPath: "/saved"
      volumes:
        - name: varlog
          hostPath:
            path: "/Users/gwonil/Documents/kubernetes-mlops/saved"
      restartPolicy: Never
  backoffLimit: 0
EOF
"""

class ExperimentUseCase:
    def __init__(self):
        self.JOB_TEMPLATE = JOB_TEMPLATE

    def start_experiment(self, experiments: List[ExperimentRequest]) -> bool:
        try:
            for i, exp in enumerate(experiments):
                args = [
                    exp.epochs,
                    exp.learning_rate,
                    exp.batch_size,
                    str(exp.learning_rate),
                    str(exp.epochs),
                    str(exp.batch_size),
                    i+1,
                ]
                run_job_cmd = self.JOB_TEMPLATE % tuple(args)
                os.system(run_job_cmd)
            return True
        except Exception as e:
            print(e)
            return False

    def experiment_list(self, repo, req: ExperimentListRequest):
        documents = repo.find(req)
        return documents