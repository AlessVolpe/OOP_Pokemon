from abc import ABCMeta

from pydantic import BaseModel


class MoveInterface(metaclass=ABCMeta, base=BaseModel):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve_move') and
                callable(subclass.move))
