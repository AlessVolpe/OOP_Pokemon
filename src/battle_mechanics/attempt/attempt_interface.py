from abc import ABCMeta

from pydantic import BaseModel


class AttemptInterface(metaclass=ABCMeta, base=BaseModel):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve_attempt') and
                callable(subclass.attempt))
