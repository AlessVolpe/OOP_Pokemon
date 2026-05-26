from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.move.move_interface import MoveInterface
from battle_mechanics.turn import Turn


class MoveWithPrecondition(MoveInterface):
    condition: ConditionInterface[Turn]
    move: MoveInterface

    def resolve_move(self) -> None:
        pass

    def __init__(self, condition, move):
        super().__init__()
        self.condition = condition
        self.move = move
