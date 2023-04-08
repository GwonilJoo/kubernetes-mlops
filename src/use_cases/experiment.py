from uuid import uuid4, UUID
from typing import List
import os

from src.domain.experiment import Experiment
from src.requests.experiment import ExperimentCreate
from src.repository.experiment import IExperimentRepository

JOB_TEMPLATE = \
"""cat << EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: model-%s-epoch-%02d-lr-%.3f-bs-%03d
spec:
  template:
    spec:
      containers:
        - name: ml
          image: gwonil/ml:latest
          resources:
            requests:
              memory: "6000Mi"
          env:
            - name: MODEL
              value: "%s"
            - name: LEARNING_RATE
              value: "%s"
            - name: EPOCHS
              value: "%s"
            - name: BATCH_SIZE
              value: "%s"
            - name: NUM_CLASSES
              value: "%s"
            - name: DB_HOST
              value: "mongo"
            - name: DB_PORT
              value: "27017"
            - name: PROJECT_ID
              value: "%s"
            - name: SAVE_DIR
              value: "/saved/models/%s/"
            - name: DATASET_DIR
              value: "/saved/dataset/%s/"
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
    def __init__(self, repo: IExperimentRepository):
        self.JOB_TEMPLATE = JOB_TEMPLATE
        self.repo = repo

    def start_experiment(
            self, 
            req: List[ExperimentCreate], 
            project_id: UUID,
            num_classes: int
        ) -> bool:
        try:
            for exp in req:
                project_id
                args = [
                    str(exp.model),
                    exp.epochs,
                    exp.learning_rate,
                    exp.batch_size,
                    str(exp.model),
                    str(exp.learning_rate),
                    str(exp.epochs),
                    str(exp.batch_size),
                    str(num_classes),
                    str(project_id),
                    str(project_id),
                    str(project_id),
                ]
                run_job_cmd = self.JOB_TEMPLATE % tuple(args)
                os.system(run_job_cmd)
            return True
        except Exception as e:
            print(e)
            return False

    def read_by_project_id(self, project_id: UUID) -> List[Experiment]:
        filters = {"project_id": project_id}
        experiments = self.repo.read_by_filters(filters)
        return experiments
    
    def delete_by_project_id(self, project_id: UUID):
        filters = {"project_id": project_id}
        experiments = self.repo.delete_many(filters)
        return experiments