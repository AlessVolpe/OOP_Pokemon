from math import floor

from battle_mechanics.effect.effect_interface import EffectInterface
from battle_mechanics.number.between import Between
from battle_mechanics.number.number import Number
from battle_mechanics.pokemon import Pokemon
from battle_mechanics.turn import Turn


class FormulaDamage(EffectInterface):
    damage: Number
    turn: Turn
    attacker: Pokemon
    defender: Pokemon

    def __init__(self):
        super().__init__()
        self.attacker = self.turn.attacker
        self.defender = self.turn.defender

    def apply(self) -> None:
        level_factor = (2 * self.attacker.level / 5) + 2
        stat_ratio = self.attacker.stats.attack / self.defender.stats.defense
        damage_calculation = (level_factor * self.attacker.chosen_move.power * stat_ratio)

        if Between(minimum=1, maximum=24, is_int=True).evaluate() is 24:
            damage_calculation = floor(damage_calculation * 1.5)
            print("It's a critical hit!")

        if self.attacker.chosen_move.move_type is any(self.attacker.types):
            damage_calculation = floor(damage_calculation * 1.5)

        if self.attacker.status is 0:
            damage_calculation = floor(damage_calculation * 0.5)

        self.damage = damage_calculation * Between(minimum=0.8, maximum=1, is_int=False).evaluate()
