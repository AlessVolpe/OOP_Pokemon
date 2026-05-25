from pydantic import BaseModel

from battle_mechanics.pokemon import Pokemon


class Turn(BaseModel):
    attacker: Pokemon
    defender: Pokemon

    def swap_attacker_defender(self) -> None:
        self.defender = self.attacker
        self.attacker = self.defender
