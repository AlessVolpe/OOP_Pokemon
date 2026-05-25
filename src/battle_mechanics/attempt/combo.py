from battle_mechanics.attempt.attempt_interface import AttemptInterface


class Combo(AttemptInterface):
    animation: Animation
    accuracy: ConditionInterface[Turn]
    hits: NumberInterface
    every: EffectInterface

    @staticmethod
    def resolve_attempts(self) -> None:
        pass

    def __init__(self, animation, accuracy, hits, every):
        self.animation = animation
        self.accuracy = accuracy
        self.hits = hits
        self.every = every
