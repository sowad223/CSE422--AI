import random

import numpy as np
def calculate_fitness(transaction_done_for_crossover, current_population):
    the_parameter_of_fitness = []
    for s in current_population:
        total_sum = 0
        for val in range(len(transaction_done_for_crossover)):
            if s[val] == 1:
                transaction_l_d_type, transaction_amount = transaction_done_for_crossover[val].split()
                if transaction_l_d_type == "l":
                    total_sum += int(transaction_amount)*(-1)
                else:
                    total_sum += int(transaction_amount)
        the_parameter_of_fitness.append(total_sum)
    return the_parameter_of_fitness


def selection(current_population, the_parameter_of_fitness):
    fit_ones = []
    for fit_people in the_parameter_of_fitness:
        fit_ones.append(fit_people / sum(the_parameter_of_fitness))
    predecures = random.choices(range(len(current_population)), weights=fit_ones, k=2)
    return current_population[predecures[0]], current_population[predecures[1]]


def crossover(chromosome_one, chromosome_two):
    point_for_cross_over= random.randint(0, (len(chromosome_one)) - 1)
    mutated_chromosome = chromosome_one[point_for_cross_over:] + chromosome_two[:point_for_cross_over]
    return mutated_chromosome


def mutation(mutated_chromosome):
    index_for_generation = random.randint(0, len(mutated_chromosome) - 1)
    mutated_chromosome[index_for_generation] = 1 - mutated_chromosome[index_for_generation]
    return mutated_chromosome


def run_genetic_algorithm(transaction_done_for_crossover, initial_population_length=10, generation_size=10000):
    initial_people = [random.randint(0, 1) for p in range((len(transaction_done_for_crossover)))]
    current_population = [initial_people[:] for p in range(initial_population_length)]

    for _ in range(generation_size):
        the_parameter_for_fitness= calculate_fitness(transaction_done_for_crossover, current_population)
        new_people = []
        for _ in range(len(current_population)):
            predecessor_one, predecessor_two = selection(current_population, the_parameter_for_fitness)
            successor = crossover( predecessor_one, predecessor_two )
            if random.random() < 0.05:
                successor = mutation(successor )
            if all(bit == 0 for bit in successor ):
                new_people.append(successor )
                continue
            if calculate_fitness(transaction_done_for_crossover, [successor])[0] == 0:
                result = ''
                for bit in successor :
                    result += str(bit)
                return result
            new_people.append(successor )
        current_population = new_people
    return -1


transactions_done_after_crossover = []
with open("input.txt", "r") as file:
    transaction_count = int(file.readline())
    for _ in range(transaction_count):
        line = file.readline().strip()
        transactions_done_after_crossover.append(line)

print(run_genetic_algorithm(transactions_done_after_crossover))
