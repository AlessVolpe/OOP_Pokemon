from battle_mechanics.attempt.attempt_interface import AttemptInterface


class Cascade(AttemptInterface):
    attempts: list[AttemptInterface]

    def resolve_attempt(self) -> None:
        pass

    def __init__(self, attempts: list[AttemptInterface]):
        super().__init__()
        self.attempts = attempts
