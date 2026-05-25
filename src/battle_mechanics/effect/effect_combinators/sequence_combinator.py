from battle_mechanics.effect.effect_interface import EffectInterface


class SequenceCombinator(EffectInterface):
    effects: list[EffectInterface]

    def __init__(self, effects: list[EffectInterface]):
        super().__init__()
        self.effects = effects

    def apply(self) -> None:
        map(apply, self.effects)
