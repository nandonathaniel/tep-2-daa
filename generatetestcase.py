import random
import numpy as np
import os

sizes = [20, 200, 2000]

if not os.path.exists('sets'):
    os.makedirs('sets')

if not os.path.exists('costs'):
    os.makedirs('costs')

for size in sizes:
    sets_filename = f'sets/set_{size}.txt'
    costs_filename = f'costs/cost_{size}.txt'
    elements = [i + 1 for i in range(size)]
    sets = []
    costs = []

    for _ in range(20):
        set_size = random.randint(1, 2*(size // 3))
        elements_in_set = random.sample(elements, set_size)
        cost = random.randint(1, 1000000)
        sets.append(elements_in_set)
        costs.append(cost)

    # Write sets to file
    with open(sets_filename, 'w') as file:
        for s in sets:
            file.write(' '.join(map(str, s)) + '\n')

    # Write costs to file
    with open(costs_filename, 'w') as file:
        file.write('\n'.join(map(str, costs)) + '\n')

print("Sets generated and saved in the 'sets' directory.")
print("Costs generated and saved in the 'costs' directory.")
