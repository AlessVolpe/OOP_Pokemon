from battle_mechanics.effect.effect_interface import EffectInterface
from battle_mechanics.pokemon import Pokemon
from battle_mechanics.target.defender import Defender



class Faint(EffectInterface):
    target: Defender

    def __init__(self, target: Defender):
        super().__init__()
        self.target = target

    def apply(self) -> None:
        self.target.turn.defender.is_fainted = True
        print("It's a one hit KO!")