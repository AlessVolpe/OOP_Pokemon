from typing import Optional

from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.effect.effect_interface import EffectInterface
from battle_mechanics.turn import Turn


class ConditionCombinator(EffectInterface):
    on_pass: Optional[EffectInterface]
    on_fail: Optional[EffectInterface]
    on_fail: EffectInterface
    condition: ConditionInterface[Turn]

    def __init__(self, on_pass: EffectInterface, on_fail: EffectInterface, effect: EffectInterface) -> None:
        super().__init__()
        self.on_pass = on_pass
        self.on_fail = on_fail
        self.effect = effect

    def apply(self) -> None:
        self.on_pass.apply() if self.condition else self.on_fail.apply()
