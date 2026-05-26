from battle_mechanics.condition.condition_interface import ConditionInterface


class BothCondition[T](ConditionInterface):
    condition: T

    def __init__(self, condition: T) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        return self.condition[0] and self.condition[1]


class EitherCondition[T](ConditionInterface):
    condition: T

    def __init__(self, condition: T) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        return self.condition[0] or self.condition[1]


class NotCondition[T](ConditionInterface):
    condition: T

    def __init__(self, condition: T) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        return not self.condition


class Chance[float](ConditionInterface):
    condition: float

    def __init__(self, condition: float) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        pass
