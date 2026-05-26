from battle_mechanics.number.number_interface import NumberInterface
from helpers.secrets_generator import secrets_generator


class Between(NumberInterface):
    minimum: float
    maximum: float
    is_int: bool

    def __int__(self, minimum: float, maximum: float, is_int: bool):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum
        self.is_int = is_int

    def evaluate(self) -> float:
        return secrets_generator.randint(self.minimum, self.maximum) if self.is_int else secrets_generator.uniform(
            self.minimum, self.maximum)
