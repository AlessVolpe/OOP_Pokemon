from battle_mechanics.number.number_interface import NumberInterface


class Number(NumberInterface):
    def __init__(self, value: float) -> None:
        super().__init__(value)

    def evaluate(self) -> float:
        return self.value