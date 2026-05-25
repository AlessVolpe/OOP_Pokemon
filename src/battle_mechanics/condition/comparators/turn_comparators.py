from typing import Any

from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.target import TargetInterface


class BattleCondition[Turn](ConditionInterface):
    turn: Turn

    def __init__(self, turn: Turn) -> None:
        self.turn = turn

    def check(self) -> bool:
        pass


class ForLifter(BattleCondition):
    target: TargetInterface

    def __init__(self, target: TargetInterface, /, **data: Any) -> None:
        super().__init__(**data)
        self.target = target
