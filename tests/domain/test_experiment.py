from uuid import uuid4
from src.domain.experiment import (
    Experiment,
    ModelType,
    Activaton,
    ValuePath,
    LastBest,
    LossAccuracy,
    Result
)


# def test_experiment_domain_init():
#     id = uuid4()
#     save_path = "/saved/experiment01.pt"
#     project_id = uuid4()

#     experiment = Experiment(
#         id=id,
#         model=ModelType.SimpleCNN,
#         epoch=10,
#         activation=Activaton.SOFTMAX,
#         dropout=0.5,
#         save_path=save_path,
#         project_id=project_id,
#     )

#     assert experiment.id == id
#     assert experiment.model == ModelType.SimpleCNN
#     assert experiment.epoch == 10
#     assert experiment.activation == Activaton.SOFTMAX
#     assert experiment.dropout == 0.5
#     assert experiment.save_path == save_path
#     assert experiment.project_id == project_id


def test_experiment_domain_from_dict():
    id = uuid4()
    project_id = uuid4()
    result = {
        "train": {
            "loss": {
                "last": {
                    "value": 0.3,
                    "save_path": "/saved/train/loss/last.pt"
                },
                "best": {
                    "value": 0.2,
                    "save_path": "/saved/train/loss/best.pt"
                }
            },
            "acc": {
                "last": {
                    "value": 0.7,
                    "save_path": "/saved/train/acc/last.pt"
                },
                "best": {
                    "value": 0.9,
                    "save_path": "/saved/train/acc/best.pt"
                }
            },
        },
        "test": {
            "loss": {
                "last": {
                    "value": 0.4,
                    "save_path": "/saved/test/loss/last.pt"
                },
                "best": {
                    "value": 0.1,
                    "save_path": "/saved/test/loss/best.pt"
                }
            },
            "acc": {
                "last": {
                    "value": 0.6,
                    "save_path": "/saved/test/acc/last.pt"
                },
                "best": {
                    "value": 0.8,
                    "save_path": "/saved/test/acc/best.pt"
                }
            },
        }
    }
    
    init_dict = {
        "id": id,
        "model": "SimpleCNN",
        "epochs": 10,
        "activation": "SOFTMAX",
        "dropout": 0.5,
        "result": result,
        "project_id": project_id,
    }

    experiment = Experiment(**init_dict)

    assert experiment.id == id
    assert experiment.model == ModelType.SimpleCNN
    assert experiment.epochs == 10
    assert experiment.activation == Activaton.SOFTMAX
    assert experiment.dropout == 0.5
    assert experiment.result == result
    assert experiment.project_id == project_id


def test_experiment_domain_to_dict():
    id = uuid4()
    project_id = uuid4()
    result = {
        "train": {
            "loss": {
                "last": {
                    "value": 0.3,
                    "save_path": "/saved/train/loss/last.pt"
                },
                "best": {
                    "value": 0.2,
                    "save_path": "/saved/train/loss/best.pt"
                }
            },
            "acc": {
                "last": {
                    "value": 0.7,
                    "save_path": "/saved/train/acc/last.pt"
                },
                "best": {
                    "value": 0.9,
                    "save_path": "/saved/train/acc/best.pt"
                }
            },
        },
        "test": {
            "loss": {
                "last": {
                    "value": 0.4,
                    "save_path": "/saved/test/loss/last.pt"
                },
                "best": {
                    "value": 0.1,
                    "save_path": "/saved/test/loss/best.pt"
                }
            },
            "acc": {
                "last": {
                    "value": 0.6,
                    "save_path": "/saved/test/acc/last.pt"
                },
                "best": {
                    "value": 0.8,
                    "save_path": "/saved/test/acc/best.pt"
                }
            },
        }
    }

    init_dict = {
        "id": id,
        "model": "SimpleCNN",
        "epochs": 10,
        "activation": "SOFTMAX",
        "dropout": 0.5,
        "result": result,
        "project_id": project_id,
    }

    experiment = Experiment(**init_dict)

    assert experiment.dict() == init_dict