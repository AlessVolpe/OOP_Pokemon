from battle_mechanics.attempt.attempt_interface import AttemptInterface
from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.effect.effect_interface import EffectInterface
from battle_mechanics.turn import Turn


class Attempt(AttemptInterface):
    accuracy: ConditionInterface[Turn]
    on_hit: EffectInterface
    on_miss: EffectInterface
    after: EffectInterface

    def resolve_attempt(self) -> None:
        pass

    def __init__(self, animation, accuracy, on_hit=None, on_miss=None, after=None):
        super.__init__()
        self.animation = animation
        self.accuracy = accuracy
        self.on_hit = on_hit
        self.on_miss = on_miss
        self.after = after
