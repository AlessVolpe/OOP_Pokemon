from battle_mechanics.move.move_interface import MoveInterface
from battle_mechanics.pokemon import Pokemon


class MoveWithApplicability(MoveInterface):
    condition: ConditionInterface[Pokemon]
    move: MoveInterface

    def resolve_move(self) -> None:
        pass

    def __init__(self, condition, move):
        self.condition = condition
        self.move = move
