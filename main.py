# I've learned how to calculate the variance of a binomial distribution.
# I've calculated that the variance of a binomial distribution,
# in the case of 5 flips of a coin, is 1.25.
# I decided to do a simulation to prove that result.

# Aprendi a calcular a variância de uma distribuição binomial.
# Calculei que a variância da distribuição binomial,
# no caso de 5 lançamentos de uma moeda, é 1.25.
# Resolvi fazer uma simulação para comprovar esse resultado.

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


###


number_successes = 0
list_variations = []
total_variations = 0

for i in range(NUMBER_SIMULATIONS):

    for i2 in range(TRIALS):
        random_number = randint(0, 1)
        if random_number == 1:
            number_successes += 1

    variation = number_successes - MEAN
    number_successes = 0

    if variation < 0:
       variation *= -1

    list_variations.append(variation)

for i3 in list_variations:
    total_variations = total_variations + i3

print(f"Absolute mean deviation: {total_variations / NUMBER_SIMULATIONS}")
