from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.pk_enums import PkType


class HasTypeCondition[Pokemon](ConditionInterface):
    condition: Pokemon
    immune_types: frozenset[PkType] = frozenset([0, 1, 2, 3, 4, 7, 8, 16, 17])

    def __init__(self, condition: Pokemon) -> None:
        self.condition = condition

    def check(self) -> bool:
        types = self.condition.Types
        return any(t in self.immune_types for t in types)


class HasMajorStatusEffectCondition[Pokemon](ConditionInterface):
    condition: Pokemon

    def __init__(self, condition: Pokemon) -> None:
        self.condition = condition

    def check(self) -> bool:
        return self.condition.status
