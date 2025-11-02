from pprint import pprint
from utils import select_a_random_chromosome, slelct_a_random_phenotype, swap

POPULATION_SIZE = 100
PARENET_SELECTION_COUNT = 5

def generate_board():
    board = []
    valid_bord_values = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(8):
        index = select_a_random_chromosome()
        board.append(valid_bord_values[index])
    return board

def generate_population(size):
    population = []
    for _ in range(size):
        population.append(generate_board())
    return population

def fitness_evaluation(queens): 
    fitness = 28
    conflicts = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j]:
                conflicts += 1
            elif abs(queens[i] - queens[j]) == abs(i - j):
                conflicts += 1
    fitness -= conflicts
    return fitness

def mution(queens):
    mut_index_1 = select_a_random_chromosome()
    mut_index_2 = select_a_random_chromosome()

    mut_el1, mut_el2 = swap(queens[mut_index_1], queens[mut_index_2])

    queens[mut_index_1] = mut_el1
    queens[mut_index_2] = mut_el2
    return queens

def parent_selection(selection_count, population=generate_population(POPULATION_SIZE)):
    parents = []
    selected_parents = []

    # Pick 5 random parents
    for _ in range(selection_count):
        random_index = slelct_a_random_phenotype(selection_count)
        parents.append(population[random_index])

    # Evaluatting Fitnesses also we sort them here! first two index will be the best parents
    for i in range(len(parents)):
        fitness = fitness_evaluation(parents[i])
        selected_parents.append({"fitness": fitness, "chromosome": parents[i]})

    return selected_parents[0], selected_parents[1]

def crossover(parent1, parent2):
    pass

def main():
    population = generate_population(POPULATION_SIZE)
    pprint(population)
    print("parents: ")
    parents= parent_selection(PARENET_SELECTION_COUNT)
    pprint(parents)
    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
