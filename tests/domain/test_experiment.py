from uuid import uuid4
from src.domain.experiment import (
    Experiment,
    ModelType,
    Activaton,
)


def test_experiment_domain_init():
    id = uuid4()
    save_path = "/saved/experiment01.pt"
    project_id = uuid4()

    experiment = Experiment(
        id=id,
        model=ModelType.SimpleCNN,
        epoch=10,
        activation=Activaton.SOFTMAX,
        dropout=0.5,
        save_path=save_path,
        project_id=project_id,
    )

    assert experiment.id == id
    assert experiment.model == ModelType.SimpleCNN
    assert experiment.epoch == 10
    assert experiment.activation == Activaton.SOFTMAX
    assert experiment.dropout == 0.5
    assert experiment.save_path == save_path
    assert experiment.project_id == project_id


def test_experiment_domain_from_dict():
    id = uuid4()
    save_path = "/saved/experiment01.pt"
    project_id = uuid4()

    init_dict = {
        "id": id,
        "model": ModelType.SimpleCNN,
        "epoch": 10,
        "activation": Activaton.SOFTMAX,
        "dropout": 0.5,
        "save_path": save_path,
        "project_id": project_id,
    }

    experiment = Experiment(**init_dict)

    assert experiment.id == id
    assert experiment.model == ModelType.SimpleCNN
    assert experiment.epoch == 10
    assert experiment.activation == Activaton.SOFTMAX
    assert experiment.dropout == 0.5
    assert experiment.save_path == save_path
    assert experiment.project_id == project_id


def test_experiment_domain_to_dict():
    id = uuid4()
    save_path = "/saved/experiment01.pt"
    project_id = uuid4()

    init_dict = {
        "id": id,
        "model": ModelType.SimpleCNN,
        "epoch": 10,
        "activation": Activaton.SOFTMAX,
        "dropout": 0.5,
        "save_path": save_path,
        "project_id": project_id,
    }

    experiment = Experiment(**init_dict)

    assert experiment.dict() == init_dict