import secrets

secretsGenerator = secrets.SystemRandom()

# Damage generators
critical_generator = secretsGenerator.randint(1, 24)
damage_die_roll = secretsGenerator.uniform(0.8, 1.0)
