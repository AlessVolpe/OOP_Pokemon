from abc import ABCMeta

from pydantic import BaseModel


class MoveInterface(BaseModel, metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve_move') and
                callable(subclass.resolve_move))

    def resolve_move(self) -> None:
        pass
