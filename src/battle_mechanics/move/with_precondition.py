from battle_mechanics.move.move_interface import MoveInterface


class MoveWithPrecondition(MoveInterface):
    condition: ConditionInterface[Turn]
    move: MoveInterface

    def resolve_move(self) -> None:
        pass

    def __init__(self, condition, move):
        self.condition = condition
        self.move = move
