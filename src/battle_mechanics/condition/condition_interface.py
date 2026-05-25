from abc import ABCMeta
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class MoveInterface(metaclass=ABCMeta, base=BaseModel):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'check') and
                callable(subclass.check))

    def check(self, condition: T) -> bool:
        pass
