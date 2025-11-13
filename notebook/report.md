# Report 
This experiment evaluates the performance of different GA configurations in solving the N-Queens problem.
Across configurations, the GA achieved a 95.8% success rate, with the PMX crossover and moderate mutation rates performing best.
Results indicate that maintaining structural consistency (PMX) and balanced exploration (mutation = 0.5) optimize convergence speed and stability.
Visual analysis confirms PMX outperformed CutFill and Multi-Cut modes in both convergence speed and variance.

#### In this note book we've tested the Simple GA with different configs combining:
- Mutation probabilities: 0.2, 0.5, 1.0
- Crossover probabilities: 0.5, 1.0
- Crossover modes: CutFill and PMX, multi-cut (1-3)
- Elitism: On and Off
- Mutation type: Bitwise and swap


| Parameter             | Values Tested                      |
| --------------------- | ---------------------------------- |
| Mutation probability  | 0.2, 0.5, 1.0                      |
| Crossover probability | 0.5, 1.0                           |
| Crossover modes       | CutFill, PMX, Multi-Cut (1–3 cuts) |
| Mutation type         | Bitwise & Swap                     |
| Elitism               | Enabled / Disabled           `      |
| Population size       | 100                                |
| Maximum generations   | 1000                               |


- Success rate: 95.8% (all but one configuration reached fitness = 1.0)
- Average generations to reach solution: ~85
- Fastest convergence: < 10 generations in several cases
- Only failure: mutation = 0.5, crossover = 1.0, mode = CutFill, no elitism (stagnated at fitness 0.5)

## Speed and Success Rate of Each Case
| Metric                        | Observation                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Best-performing crossover** | PMX consistently reached the solution in fewer generations and showed more stable convergence across different mutation rates. |
| **CutFill**                   | Worked well in moderate mutation/crossover settings but tended to stagnate at extreme probabilities.                           |
| **Multi-Cut (2–3 cuts)**      | Sometimes improved diversity and exploration but didn’t always outperform PMX.                                                 |
| **Elitism**                   | Slightly increased stability but occasionally slowed convergence when diversity was reduced.                                   |
| **Mutation Rate**             | A mid-range mutation rate (0.5) provided the best balance of diversity and stability.                                          |

<br>

| Setting                         | Performance            | Explanation                                                                                             |
| ------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------- |
| **Crossover Mode = PMX**        | Best overall         | PMX maintains mapping between parent genes, preserving permutation validity and structural inheritance. |
| **Mutation Probability = 0.5**  | Balanced            | Provides enough diversity to escape local minima without losing structure.                              |
| **Crossover Probability = 1.0** | Fast Convergence | Ensures crossover is always applied, improving exploration speed.                                       |
| **Elitism = False**             | Slightly faster     | Prevents premature convergence by avoiding overprotection of top individuals.                           |
| **Multi-Cut = 1–2 cuts**        | Good diversity      | Multi-cut helps when population stagnates but beyond 2 cuts, disruption outweighs benefit.              |

<br>


  

### Convergence Speed by Mutation Rate & Crossover Mode

  

**Lower = faster convergence**

  

Shows that PMX was the most reliable operator across all mutation levels, with CutFill lagging slightly, especially at high mutation rates.

  

Interpretation: PMX preserves relative order and mapping, helping maintain valid permutations. CutFill, in contrast, may introduce more disruption between parent and child genes.

  

**Boxplot — Variability in Generations per Crossover Mode**

  

-  Smaller box = more stable behavior

  

PMX not only converged faster but also with less variance — indicating better stability.

CutFill showed wider variation (sensitive to randomness), while Multi-Cut had moderate variance.

  

Interpretation: PMX is more robust for permutation problems where positional consistency matters.

  

**Elitism vs. Non-Elitism**

  

Shows average generations with and without elitism.

Elitism slightly increased stability, but at times delayed convergence because top chromosomes dominated too early, reducing diversity.

  

Interpretation: For small populations, elitism offers limited advantage; the GA naturally maintains top solutions without needing strict elitist preservation.‍‍

  

**Multi-Cut Crossover Comparison**

  

When varying the number of crossover cuts:

  

1-cut (simple split): fastest convergence (less disruption)

  

2–3 cuts: improved exploration but slower average convergence

  

Interpretation: Higher cuts increase diversity but disrupt gene continuity; the optimal cut count is usually 1–2 for the N-Queens problem.


The GA exhibited strong exploitation through fitness-based selection and crossover inheritance, and controlled exploration through mutation and randomized crossover points.

Exploration mainly came from:

Bitwise mutation (reintroducing lost gene diversity)

Multi-cut crossover (shuffling multiple gene segments)

Exploitation came from:

Fitness sorting and elitism

PMX crossover (preserving gene mapping)

The best configurations achieved a dynamic balance — sufficient exploration early on, gradually shifting to exploitation as fit individuals dominated.


### Conclusions

The GA successfully solved the N-Queens problem in nearly all configurations.
However, parameter tuning had a large effect on speed and reliability.

PMX crossover → best stability and fastest convergence

Balanced mutation → prevents stagnation

Elitism → good for stability, not for speed

Multi-cut → offers exploration but adds computational noise
