from abc import ABCMeta
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class ConditionInterface[T](BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'check') and
                callable(subclass.check))

    def check(self) -> bool:
        pass
