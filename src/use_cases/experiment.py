from uuid import uuid4, UUID
from typing import List
import os

from src.domain.experiment import Experiment
from src.requests.experiment import ExperimentRequest, ExperimentListRequest


class ExperimentUseCase:
    def __init__(self):
        # self.JOB_TEMPLATE = \
        #     """cat << EOF | kubectl apply -f -
        #     apiVersion: batch/v1
        #     kind: Job
        #     metadata:
        #     name: exp%02d
        #     spec:
        #     template:
        #         spec:
        #         containers:
        #         - name: ml
        #             image: %s
        #             command: ["python", "train.py"]
        #             args: ['%s', '%s', '%s']
        #             resources:
        #             limits:
        #                 cpu: "1"
        #                 memory: "6Gi"
        #         restartPolicy: Never
        #     EOF
        #     """
        
        self.JOB_TEMPLATE = ""
        self.JOB_TEMPLATE += "docker run -itd --rm "
        self.JOB_TEMPLATE += "-e LEARNING_RATE=%s "
        self.JOB_TEMPLATE += "-e EPOCHS=%s "
        self.JOB_TEMPLATE += "-e BATCH_SIZE=%s "
        self.JOB_TEMPLATE += "-e EXPERIMENT_ID=%s "
        self.JOB_TEMPLATE += "--network %s "
        self.JOB_TEMPLATE += "--name ml-%s "
        self.JOB_TEMPLATE += "ml:latest"


    def start_experiment(self, experiments: List[ExperimentRequest]) -> bool:
        try:
            for i, exp in enumerate(experiments):
                args = [
                    exp.learngin_rate,
                    exp.epochs,
                    exp.batch_size,
                    str(uuid4()),
                    "docker-env_default",
                    i,
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