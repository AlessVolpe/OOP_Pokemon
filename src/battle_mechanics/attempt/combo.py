from battle_mechanics.attempt.attempt_interface import AttemptInterface
from battle_mechanics.condition.condition_interface import ConditionInterface
from battle_mechanics.effect.effect_interface import EffectInterface
from battle_mechanics.number.number import Number
from battle_mechanics.number.number_interface import NumberInterface
from battle_mechanics.turn import Turn


class Combo(AttemptInterface):
    accuracy: ConditionInterface[Turn]
    hits: Number
    every: EffectInterface

    def resolve_attempt(self) -> None:
        pass

    def __init__(self, accuracy, hits, every):
        super().__init__()
        self.accuracy = accuracy
        self.hits = hits
        self.every = every
