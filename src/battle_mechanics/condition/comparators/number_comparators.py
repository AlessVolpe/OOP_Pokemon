from battle_mechanics.condition.condition_interface import ConditionInterface


class LessThanCondition[NumberInterface](ConditionInterface):
    condition: NumberInterface

    def __init__(self, condition: NumberInterface) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        pass


class GreaterThanCondition[NumberInterface](ConditionInterface):
    condition: NumberInterface

    def __init__(self, condition: NumberInterface) -> None:
        super().__init__()
        self.condition = condition

    def check(self) -> bool:
        pass
