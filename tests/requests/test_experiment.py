from uuid import uuid4
from src.requests.experiment import ExperimentRequest
from src.domain.experiment import ModelType, Activaton


def test_experiment_request_init():
    save_dir = "/saved/experiment01.pt"
    project_id = uuid4()

    experiment = ExperimentRequest(
        model=ModelType.SimpleCNN,
        epochs=10,
        activation=Activaton.SOFTMAX,
        dropout=0.5,
        save_dir=save_dir,
        project_id=project_id,
    )

    assert experiment.model == ModelType.SimpleCNN
    assert experiment.epochs == 10
    assert experiment.activation == Activaton.SOFTMAX
    assert experiment.dropout == 0.5
    assert experiment.save_dir == save_dir
    assert experiment.project_id == project_id


def test_experiment_domain_from_dict():
    save_dir = "/saved/experiment01.pt"
    project_id = uuid4()

    init_dict = {
        "model": ModelType.SimpleCNN,
        "epochs": 10,
        "activation": Activaton.SOFTMAX,
        "dropout": 0.5,
        "save_dir": save_dir,
        "project_id": project_id,
    }

    experiment = ExperimentRequest(**init_dict)

    assert experiment.model == ModelType.SimpleCNN
    assert experiment.epochs == 10
    assert experiment.activation == Activaton.SOFTMAX
    assert experiment.dropout == 0.5
    assert experiment.save_dir == save_dir
    assert experiment.project_id == project_id


def test_experiment_domain_to_dict():
    save_dir = "/saved/experiment01.pt"
    project_id = uuid4()

    init_dict = {
        "model": ModelType.SimpleCNN,
        "epochs": 10,
        "activation": Activaton.SOFTMAX,
        "dropout": 0.5,
        "save_dir": save_dir,
        "project_id": project_id,
    }

    experiment = ExperimentRequest(**init_dict)

    assert experiment.dict() == init_dict