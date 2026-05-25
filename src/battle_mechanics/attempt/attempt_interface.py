from abc import ABCMeta

from pydantic import BaseModel


class AttemptInterface(BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve_attempt') and
                callable(subclass.resolve_attempt))

    def resolve_attempt(self) -> None:
        pass
