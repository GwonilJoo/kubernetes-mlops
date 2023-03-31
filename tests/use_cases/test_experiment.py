import pytest
from uuid import uuid4
from unittest import mock

from src.domain.experiment import (
    Experiment,
    ModelType,
    Activaton,
    Result,
    LossAcc,
    LastBest,
    ValuePath
)
from src.use_cases.experiment import ExperimentUseCase


@pytest.fixture
def domain_experiments():
    exp_1 = Experiment(
        id=uuid4(),
        model=ModelType.SimpleCNN,
        epochs=10,
        activation=Activaton.LINEAR,
        dropout=0.1,
        result=Result(
            train=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.1,
                        save_path="/saved/train/loss/last/0.1.pt"
                    ),
                    best=ValuePath(
                        value=0.01,
                        save_path="/saved/train/loss/best/0.01.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.9,
                        save_path="/saved/train/acc/last/0.9.pt"
                    ),
                    best=ValuePath(
                        value=0.99,
                        save_path="/saved/train/acc/best/0.99.pt"
                    )
                ),
            ),
            test=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.11,
                        save_path="/saved/test/loss/last/0.11.pt"
                    ),
                    best=ValuePath(
                        value=0.011,
                        save_path="/saved/test/loss/best/0.011.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.91,
                        save_path="/saved/test/acc/last/0.91.pt"
                    ),
                    best=ValuePath(
                        value=0.991,
                        save_path="/saved/test/acc/best/0.991.pt"
                    )
                ),
            ),
        ),
        project_id=uuid4(),
    )

    exp_2 = Experiment(
        id=uuid4(),
        model=ModelType.SimpleCNN,
        epochs=20,
        activation=Activaton.LINEAR,
        dropout=0.2,
        result=Result(
            train=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.2,
                        save_path="/saved/train/loss/last/0.2.pt"
                    ),
                    best=ValuePath(
                        value=0.02,
                        save_path="/saved/train/loss/best/0.02.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.8,
                        save_path="/saved/train/acc/last/0.8.pt"
                    ),
                    best=ValuePath(
                        value=0.88,
                        save_path="/saved/train/acc/best/0.88.pt"
                    )
                ),
            ),
            test=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.22,
                        save_path="/saved/test/loss/last/0.22.pt"
                    ),
                    best=ValuePath(
                        value=0.022,
                        save_path="/saved/test/loss/best/0.022.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.81,
                        save_path="/saved/test/acc/last/0.81.pt"
                    ),
                    best=ValuePath(
                        value=0.881,
                        save_path="/saved/test/acc/best/0.881.pt"
                    )
                ),
            ),
        ),
        project_id=uuid4(),
    )

    exp_3 = Experiment(
        id=uuid4(),
        model=ModelType.SimpleCNN,
        epochs=30,
        activation=Activaton.LINEAR,
        dropout=0.3,
        result=Result(
            train=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.3,
                        save_path="/saved/train/loss/last/0.3.pt"
                    ),
                    best=ValuePath(
                        value=0.03,
                        save_path="/saved/train/loss/best/0.03.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.7,
                        save_path="/saved/train/acc/last/0.7.pt"
                    ),
                    best=ValuePath(
                        value=0.77,
                        save_path="/saved/train/acc/best/0.77.pt"
                    )
                ),
            ),
            test=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.33,
                        save_path="/saved/test/loss/last/0.33.pt"
                    ),
                    best=ValuePath(
                        value=0.033,
                        save_path="/saved/test/loss/best/0.033.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.71,
                        save_path="/saved/test/acc/last/0.71.pt"
                    ),
                    best=ValuePath(
                        value=0.771,
                        save_path="/saved/test/acc/best/0.771.pt"
                    )
                ),
            ),
        ),
        project_id=uuid4(),
    )

    exp_4 = Experiment(
        id=uuid4(),
        model=ModelType.SimpleCNN,
        epochs=40,
        activation=Activaton.LINEAR,
        dropout=0.4,
        result=Result(
            train=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.4,
                        save_path="/saved/train/loss/last/0.4.pt"
                    ),
                    best=ValuePath(
                        value=0.04,
                        save_path="/saved/train/loss/best/0.04.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.6,
                        save_path="/saved/train/acc/last/0.6.pt"
                    ),
                    best=ValuePath(
                        value=0.66,
                        save_path="/saved/train/acc/best/0.66.pt"
                    )
                ),
            ),
            test=LossAcc(
                loss=LastBest(
                    last=ValuePath(
                        value=0.44,
                        save_path="/saved/test/loss/last/0.44.pt"
                    ),
                    best=ValuePath(
                        value=0.044,
                        save_path="/saved/test/loss/best/0.044.pt"
                    )
                ),
                acc=LastBest(
                    last=ValuePath(
                        value=0.61,
                        save_path="/saved/test/acc/last/0.61.pt"
                    ),
                    best=ValuePath(
                        value=0.661,
                        save_path="/saved/test/acc/best/0.661.pt"
                    )
                ),
            ),
        ),
        project_id=uuid4(),
    )

    return [exp_1, exp_2, exp_3, exp_4]


def test_room_list_without_parameters(domain_experiments): 
    repo = mock.Mock()
    experiment_use_case = ExperimentUseCase()

    repo.list.return_value = domain_experiments
    result = experiment_use_case.experiment_list(repo, )
    repo.list.assert_called_with()
    assert result == domain_experiments