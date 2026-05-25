from battle_mechanics.number.number_interface import NumberInterface
from helpers.secrets_generator import secrets_generator


class Between(NumberInterface):
    maximum: float

    def __int__(self, maximum: float, minimum: float):
        super().__init__(minimum)
        self.maximum = maximum

    def evaluate(self) -> float:
        return secrets_generator.uniform(self.value, self.maximum)