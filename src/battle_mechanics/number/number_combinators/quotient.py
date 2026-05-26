from battle_mechanics.number.number import Number
from battle_mechanics.number.number_interface import NumberInterface


class Sum(NumberInterface):
    a: Number
    b: Number

    def __init__(self, a: Number, b: Number) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def evaluate(self) -> float:
        return self.a.evaluate() / self.b.evaluate()
