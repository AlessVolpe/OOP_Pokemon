from abc import ABCMeta, abstractmethod

from pydantic import BaseModel


class EffectInterface(BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'apply') and
                callable(subclass.apply))

    @abstractmethod
    def apply(self) -> None:
        pass
