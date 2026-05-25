from typing import Annotated, Optional

from pydantic import Field

from battle_mechanics.attempt.attempt_interface import AttemptInterface
from battle_mechanics.move.move_interface import MoveInterface
from battle_mechanics.pk_enums import PkType, MoveSubcategory


class Move(MoveInterface):
    move_name: str
    move_type: PkType
    power: int
    pp: Annotated[int, Field(..., gt=0)]
    move_subcategory: Optional[MoveSubcategory]
    attempt: AttemptInterface

    @staticmethod
    def resolve_move(self) -> None:
        pass

    def __init__(self, move_name, move_type, power, pp, move_subcategory, attempt):
        self.move_name = move_name
        self.move_type = move_type
        self.power = power
        self.pp = pp
        self.move_subcategory = move_subcategory
        self.attempt = attempt
