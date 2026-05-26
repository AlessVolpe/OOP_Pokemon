from battle_mechanics.number.number_interface import NumberInterface


class Number(NumberInterface):
    value: float

    def __init__(self, value: float) -> None:
        super().__init__()
        self.value = value

    def evaluate(self) -> float:
        return self.value
