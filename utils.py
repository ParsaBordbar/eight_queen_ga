import random
from configs import CONFIG as cfg

def swap(item1, item2):
    return item2, item1

def select_a_random_chromosome(N=cfg.n_queens):
    return random.randint(0, N - 1)

def select_a_random_phenotype(population_size):
    return random.randint(0, population_size - 1)

def generate_chromosome(N=cfg.n_queens):
    return random.sample(range(N), N)

def ga_summary(
        original_population,
        parents,
        crossover_result,
        crossover_mode,
        mutated_children,
        surival_selection_type,
        mean_fitness, evaluations):

    print("\n├──----[ GA Round Summary ]-----")
    print(f"├──> Evaluations: {evaluations}")
    print(f"├──> Original Population Size: {len(original_population)}")
    print(f"├── Selected Parents:")
    print("├──>", parents)
    print(f"├── Crossver Oprator: {crossover_mode}")
    print(f"├── Crossover Result:")
    print("├──>", crossover_result)
    print(f"├──> Survival Selection Type: {surival_selection_type}")
    print(f"├──> Mutated Children:")
    print("├──", mutated_children)
    print(f"└──[ Mean Fitness: {mean_fitness} ]----\n")