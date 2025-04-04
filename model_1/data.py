from model import Creation


creations: list[Creation] = [
    Creation(
        name='Alex',
        country='Russia',
        area='Moscow region',
        description='Python developer',
        slug='alex'
        ),
    Creation(
        name='AlexFil',
        country='Russia',
        area='Moscow region',
        description='ML developer',
        slug='alexfil'
        ),
]


def get_creations() -> list[Creation]:
    return creations
