from random import randint

number_successes = 0
list_variations_squared = []
total_variations_squared = 0
NUMBER_SIMULATIONS = 10000
TRIALS = 5
MEAN = 2.5

for i in range(NUMBER_SIMULATIONS):

    for i2 in range(TRIALS):
        random_number = randint(0, 1)
        if random_number == 1:
            number_successes += 1

    variation = number_successes - MEAN
    number_successes = 0

    variation_squared = variation * variation
    list_variations_squared.append(variation_squared)

for i3 in list_variations_squared:
    total_variations_squared = total_variations_squared + i3

print(f"Variance: {total_variations_squared / NUMBER_SIMULATIONS}")

