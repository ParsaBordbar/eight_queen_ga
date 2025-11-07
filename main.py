import random
from configs import CONFIG as cfg
from utils import ga_summary, generate_chromosome, select_a_random_chromosome, select_a_random_phenotype


def generate_population(size, N=cfg.n_queens):
    return [generate_chromosome(N) for _ in range(size)]

def fitness_evaluation(queens):
    penalty = 0
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i] == queens[j]:
                penalty += 1
            elif abs(queens[i] - queens[j]) == abs(i - j):
                penalty += 1
    fitness = 1 / (1 + penalty)
    return round(fitness, 3)


def parent_selection(selection_count, population):
    sample = [population[select_a_random_phenotype(len(population) - 1)]
              for _ in range(selection_count)]
    parents = [{"fitness": fitness_evaluation(s), "chromosome": s} for s in sample]
    parents.sort(key=lambda x: x['fitness'], reverse=True)
    return parents[0], parents[1]


def crossover(parent1, parent2, prob=cfg.crossover_probability, mode="cutfill", cuts=1):
    if random.random() > prob:
        return [parent1[:], parent2[:]]

    N = len(parent1)

    # === CUT-AND-FILL (default) ===
    if mode == "cutfill":
        crossover_point = select_a_random_chromosome(N)
        if crossover_point < 1:
            crossover_point = 3

        p1_first = parent1[:crossover_point]
        p2_cycle = parent2[crossover_point:] + parent2[:crossover_point]
        child1_tail = [g for g in p2_cycle if g not in p1_first][: N - crossover_point]
        child1 = p1_first + child1_tail

        p2_first = parent2[:crossover_point]
        p1_cycle = parent1[crossover_point:] + parent1[:crossover_point]
        child2_tail = [g for g in p1_cycle if g not in p2_first][: N - crossover_point]
        child2 = p2_first + child2_tail
        return [child1, child2]

    #PMX CROSSOVER
    if mode == "pmx":
        c1, c2 = sorted(random.sample(range(N), 2))
        child1, child2 = parent1[:], parent2[:]

        child1[c1:c2], child2[c1:c2] = parent2[c1:c2], parent1[c1:c2]

        # mapping
        mapping1 = {parent2[i]: parent1[i] for i in range(c1, c2)}
        mapping2 = {parent1[i]: parent2[i] for i in range(c1, c2)}

        # fix duplicates
        def map_gene(gene, mapping):
            while gene in mapping:
                gene = mapping[gene]
            return gene

        for i in list(range(0, c1)) + list(range(c2, N)):
            child1[i] = map_gene(child1[i], mapping1)
            child2[i] = map_gene(child2[i], mapping2)
        return [child1, child2]

    #MULTI-CUT (2 or 3 cuts)
    if mode == "multi":
        cuts = min(cuts, 3)
        cut_points = sorted(random.sample(range(1, N - 1), cuts))
        parts1, parts2 = [], []
        last = 0
        for cp in cut_points + [N]:
            parts1.append(parent1[last:cp])
            parts2.append(parent2[last:cp])
            last = cp
        child1, child2 = [], []
        for i in range(len(parts1)):
            if i % 2 == 0:
                child1 += parts1[i]
                child2 += parts2[i]
            else:
                child1 += parts2[i]
                child2 += parts1[i]
        return [child1, child2]
    return [parent1[:], parent2[:]]


def mutation(chromosome, prob=cfg.mutation_probability, mode=cfg.mutation_type):
    if random.random() > prob:
        return chromosome

    N = len(chromosome)
    i, j = select_a_random_chromosome(N), select_a_random_chromosome(N)
    if mode == "swap":
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    elif mode == "bitwise":
        chromosome[i] = random.choice([x for x in range(N) if x not in chromosome or x == chromosome[i]])
    return chromosome


def survival_selection(population, children, population_size=cfg.population_size):
    all_samples = population + children
    fitnesses = [{"fitness": fitness_evaluation(s), "chromosome": s} for s in all_samples]
    fitnesses.sort(key=lambda x: x['fitness'], reverse=True)
    return [f["chromosome"] for f in fitnesses[:population_size]]


def fitness_mean(population):
    return round(sum(fitness_evaluation(s) for s in population) / len(population), 4)


def simple_GA_pipeline(rounds=cfg.ga_pipeline_rounds,
                       population_size=cfg.population_size,
                       parent_selection_count=cfg.parent_selection_count,
                       N=cfg.n_queens):
    population = generate_population(population_size, N)
    evaluations = 0

    for gen in range(rounds):
        parents = parent_selection(parent_selection_count, population)
        evaluations += len(parents)

        crossover_result = crossover(parents[0]['chromosome'], parents[1]['chromosome'])
        evaluations += 2

        children = [mutation(c, cfg.mutation_probability, cfg.mutation_type) for c in crossover_result]
        evaluations += len(children)

        population = survival_selection(population, children, population_size)
        mean_fitness = fitness_mean(population)

        ga_summary(population, parents, crossover_result, children, population, population, mean_fitness, evaluations)

        if any(fitness_evaluation(p) == 1 for p in population):
            print(f"✅ Solution found at generation {gen} after {evaluations} evaluations!")
            break
        if evaluations >= cfg.max_evaluations:
            print("⚠️ Terminated after reaching evaluation limit.")
            break

    return population


def main():
    simple_GA_pipeline(rounds=500, population_size=cfg.population_size, parent_selection_count=cfg.parent_selection_count, N=cfg.n_queens)

if __name__ == "__main__":
    main()
