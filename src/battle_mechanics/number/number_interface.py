from abc import ABCMeta

from pydantic import BaseModel


class NumberInterface(BaseModel, metaclass=ABCMeta):
    value: float

    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = value

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'evaluate') and
                callable(subclass.evaluate))

    def evaluate(self) -> float:
        pass
