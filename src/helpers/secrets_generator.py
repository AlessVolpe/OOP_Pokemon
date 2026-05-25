import secrets
from logging import critical

secrets_generator = secrets.SystemRandom()

critical_generator = secrets_generator.randint(1,24)
damage_die_roll = secrets_generator.uniform(0.8, 1.0)
