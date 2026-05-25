from battle_mechanics.effect.effect_interface import EffectInterface


class FormulaDamage(EffectInterface):
    damage: NumberInterface

    def __init__(self, damage):
        super().__init__()
        self.damage = damage

    def apply(self) -> None:
        pass
