from battle_mechanics.number.number_interface import NumberInterface


class Sum(NumberInterface):
    a: NumberInterface
    b: NumberInterface

    def __init__(self, a: NumberInterface, b: NumberInterface, value) -> None:
        super().__init__(value)
        self.a = a
        self.b = b

    def evaluate(self) -> float:
        return self.a.value / self.b.value