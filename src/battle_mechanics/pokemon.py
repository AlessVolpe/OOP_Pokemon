from typing import Optional, Annotated, Any

from pydantic import BaseModel, Field

from battle_mechanics.move.move import MoveInterface
from battle_mechanics.pk_enums import PkType, StatusEffect
from helpers.type_helpers import ValueRange


class Stats(BaseModel):
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int

    def __init__(self, hp, attack, defense, sp_atk, sp_def, speed, /, **data: Any):
        super().__init__(**data)
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed


class Pokemon(BaseModel):
    name: str
    nickname: Optional[str]
    types: PkType | tuple[PkType, PkType]
    level: Annotated[int, ValueRange(1, 100)]
    stats: Stats
    moves: list[MoveInterface] = Field(..., min_length=1, max_length=4)
    status: Optional[StatusEffect]
    is_fainted: bool = False

    def __init__(self, name, nickname, types, level, stats, moves, status, is_fainted, **data: Any):
        super().__init__(**data)
        self.name = name
        self.nickname = nickname
        self.types = types
        self.level = level
        self.stats = stats
        self.moves = moves
        self.status = status
        self.is_fainted = is_fainted
