import numpy as np
import random

rng = random.Random(id)
shuffled_cards = range(20)
rng.shuffle(shuffled_cards)

print shuffled_cards