from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class AttemptInterface(BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve_attempt') and
                callable(subclass.resolve_attempt))

    @abstractmethod
    def resolve_attempt(self) -> None:
        pass
