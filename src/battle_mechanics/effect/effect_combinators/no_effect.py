from battle_mechanics.effect.effect_interface import EffectInterface


class NoEffect(EffectInterface):
    effect: None = None

    def __init__(self) -> None:
        super().__init__()

    def apply(self) -> None:
        pass
