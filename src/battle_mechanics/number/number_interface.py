from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class NumberInterface(BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'evaluate') and
                callable(subclass.evaluate))

    @abstractmethod
    def evaluate(self) -> float:
        pass
