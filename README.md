
# Eight Queen's Problem with Simple GA

<img width="400" height="400" alt="8queens" src="https://github.com/user-attachments/assets/bb062757-1e77-4bde-a417-d018de3b22ca" />



This project implements a Genetic Algorithm (GA) to solve the 8-Queens problem — placing 8 queens on a chessboard such that no two queens attack each other.
The algorithm evolves a population of candidate solutions through selection, crossover, mutation, and survival selection.


### Problem Definition

The 8-Queens problem asks:

“How can 8 queens be placed on a standard chessboard so that no two queens threaten each other?”

In this representation:
	•	A chromosome is an array of length 8.
	•	Each element represents the row position of the queen in a given column.
Example:

Chromosome = [4, 2, 7, 3, 6, 8, 5, 1]

means:
	•	Queen in column 1 is in row 4,
	•	Queen in column 2 is in row 2, etc.


## Genetic Algorithm Overview

The algorithm follows the classic GA pipeline:
	1.	Initialization — Randomly generate a population of candidate chromosomes.
	2.	Fitness Evaluation — Compute how “good” each solution is.
	3.	Parent Selection — Choose the best chromosomes for reproduction.
	4.	Crossover — Combine parents to create offspring.
	5.	Mutation — Randomly alter genes to introduce variation.
	6.	Survival Selection — Choose the best individuals for the next generation.
	7.	Repeat — Continue evolving until reaching the best fitness or maximum rounds.



###  Parameters

Variable	Description	Default
POPULATION_SIZE	Number of chromosomes in each generation	100
PARENET_SELECTION_COUNT	Number of parents to select for reproduction	5
GA_PIPLINE_ROUNDS	Number of generations (iterations)	50



## Function-by-Function Explanation

**1. generate_population(size)**

Generates an initial population of random chromosomes using generate_chromosome() from utils.py.
```
def generate_population(size):
    population = []
    for _ in range(size):
        population.append(generate_chromosome())
    return population
```
Purpose: Create diversity in the initial population.
Output: List of chromosomes (each representing a queen placement).


**2. fitness_evaluation(queens)**

Evaluates how good a chromosome is by counting the number of conflicts.
```
def fitness_evaluation(queens):
    ...
    fitness = 1 / (1 + penalty)
```
Explanation:
	•	A penalty is added when:
	•	Two queens share the same row.
	•	Two queens share the same diagonal.
	•	The fitness is inversely proportional to the penalty:
	•	Fewer conflicts → Higher fitness
	•	Perfect solution → Fitness = 1.0


**3. parent_selection(selection_count, population)**

Selects random chromosomes as potential parents, evaluates them, and returns the top two with the best fitness.
```
def parent_selection(selection_count, population):
    ...
    return parents[0], parents[1]
```
Purpose: Mimic natural selection by favoring fitter chromosomes for reproduction.


**4. crossover(parent1, parent2)**

Performs partially mapped crossover (PMX) on two parent chromosomes to create two children.
```
def crossover(parent1, parent2):
    crossover_point = select_a_random_chromosome()
    ...
    return [child1, child2]
```
Steps:
	1.	Randomly select a crossover point.
	2.	Split each parent into two parts.
	3.	Combine and rearrange the genes ensuring no duplicates.
	4.	Produce two children that mix features from both parents.

Purpose: Recombine good traits from both parents to explore new solutions.


**5. mution(queen)**

Performs a swap mutation — swaps the position of two randomly chosen genes.

```
def mution(queen):
    mut_index_1 = select_a_random_chromosome()
    mut_index_2 = select_a_random_chromosome()
```
Purpose:
Introduce randomness and maintain diversity to avoid local optima.


**6. survival_selection(population, children)**

Selects the fittest chromosomes between the old population and the new children for the next generation.

```
def survival_selection(population, children, population_size=POPULATION_SIZE):
    ...
    return population_fitnesses[:population_size]
```
Purpose:
Keep the best solutions (“survival of the fittest”) to form the next generation.


**7. fitness_mean(population)**

Computes the mean fitness of the population for progress tracking.

```
def fitness_mean(population):
    total_fitness = sum(fitness_evaluation(sample) for sample in population)
    return (total_fitness / len(population)).__round__(4)
```

**8. simple_GA_pipline(rounds, population_size, parent_selection_count)**

Main evolutionary loop of the algorithm.
```
def simple_GA_pipline(...):
    population = generate_population(population_size)
    for _ in range(rounds):
        parents = parent_selection(...)
        crossover_result = crossover(...)
        ...
        ga_summary(...)
```
**Pipeline steps:**
	1.	Generate initial population.
	2.	Select parents.
	3.	Apply crossover and mutation.
	4.	Evaluate fitness.
	5.	Perform survival selection.
	6.	Log generation summary via ga_summary().


**9. main()**

Entry point of the program.
```
def main():
   simple_GA_pipline(10, POPULATION_SIZE, PARENET_SELECTION_COUNT)
```

#### Example Output

Crossover point at index: 4 

Child 1 [4, 2, 7, 3, 6, 8, 5, 1]
Child 2 [1, 5, 8, 6, 3, 7, 2, 4]

Children's fitnesses: 
[{'fitness': 0.5, 'chromosome': [4, 2, 7, 3, 6, 8, 5, 1]}, ... ]

```
----- GA Summary -----
Original Population Size: 100
Mean Fitness: 0.83
```



##  Utilities (utils.py)

Make sure your utils.py includes:
	•	generate_chromosome() → Creates random chromosome [1..8]
	•	select_a_random_chromosome() → Returns random index (0–7)
	•	slelct_a_random_phenotype() → Returns random individual index
	•	swap(a, b) → Swaps two values
	•	ga_summary(...) → Prints or logs each generation’s results



##  Running the Program
you can run it using uv:
```
uv run main.py
```
or with python3
```
python3 main.py
```
You can tweak:
	•	Population size
	•	Mutation rate (via function behavior)
	•	Number of rounds

to experiment with the algorithm’s performance.

