from enum import auto

from src.utils import StrEnum


def test_str_enum():
    class Sample(StrEnum):
        CLASS = auto()
        FUNCTION = auto()

    assert Sample.CLASS == "CLASS"
    assert Sample.FUNCTION == "FUNCTION"