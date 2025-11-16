# **Genetic Algorithm Report — N-Queens**

This assignment evaluates the performance of different Genetic Algorithm (GA) configurations on the **8-Queens** problem using combinations of crossover types, mutation types, mutation rates, crossover probabilities, elitism, and multi-cut crossover variants.

Across all configurations, the GA achieved a **96.8% success rate**, failing only in a few extreme configurations (mostly multi-cut with stagnation).

Most runs converged very quickly — many in **0 to 10 generations**, with rare outliers up to the 900–1000 generation limit.

The results show clear patterns:

- **PMX crossover remains the most stable overall**
- **CutFill benefits strongly from swap mutation**
- **Multi-cut crossover is chaotic but occasionally extremely fast**
- **Elitism improves reliability but sometimes increases generation count**
- **Mutation rates 0.5–1.0 with swap or bitwise lead to the best outcomes**

---

# **Parameters Tested**

| Parameter | Values |
| --- | --- |
| Mutation probability | 0.2, 0.5, 1.0 |
| Mutation type | bitwise, swap |
| Crossover probability | 0.5, 1.0 |
| Crossover mode | cutfill, PMX, multi-cut (1–3 cuts) |
| Elitism | True / False |
| Population size | 100 |
| Max generations | 1000 |

---

# **Overall Results Summary**

### **Success Rate:** **96.8%**

Only **10 failures** out of 312 total runs (mostly multi-cut mode combined with certain mutation types).

### **Average generations to solution:**

**~78 generations** (median is much lower due to many instant solutions)

### **Fastest convergence:**

**Generation 0** in multiple cases

(e.g., cutfill, multi-cut, PMX — particularly with swap mutation)

### **Slowest successful case:**

~883 generations

(multi-cut with swap mutation)

### **Failure patterns:**

Most failures occur where diversity collapses early — common in

- multi-cut with swap mutation
- elitism ON + high mutation sometimes clash
- extremely noisy search with bitwise mutation + multi-cut (rare)

---

# **Performance**

![speed_by_mutation_mode.png](attachment:78a601f7-4958-4c1e-9c97-abb7e59a801b:speed_by_mutation_mode.png)

## **Best Overall Configuration**

Across all data:

| Parameter | Best Values |
| --- | --- |
| **Crossover mode** | **PMX** |
| **Mutation probability** | **0.5 – 1.0** |
| **Crossover probability** | **1.0** |
| **Mutation type** | **swap** (quickest), bitwise (stable) |
| **Elitism** | **OFF** (faster), ON (more consistent) |
| **Multi-cut** | **1–2 cuts** if used |

PMX still demonstrates the most consistent convergence across mutation types and probabilities.

---

# **Mode-by-Mode Summary**

![distribution_by_mode.png](attachment:d1135bce-3a1e-4d01-888f-25c8b202ee8b:distribution_by_mode.png)

### **PMX Crossover — Most Stable & Efficient**

- Rarely fails
- Converges quickly (often <100 generations)
- Strong structure preservation helps permutation problems
- Works well with both mutation types

**Example:**

- mutation=0.5, pmx → 31–81 generations
- mutation=1.0, pmx → many instant solutions (gen 0 or gen ≤60)

---

### **CutFill Crossover — Fast with Swap Mutation**

CutFill often converges **instantly** with swap mutation:

- mutation=0.5, swap → **generation 0**
- mutation=1.0, swap → often ≤100 generations

But bitwise mutation versions can become unstable when elitism is ON.

---

### **Multi-Cut Crossover — High Variance (Exploration-Heavy)**

Multi-cut crossover behaves chaotically:

- Sometimes extremely fast (gen 0–5)
- Sometimes extremely slow (gen 800–999)
- Rare failures (fitness stuck at 0.5)

**Patterns:**

- 1-cut is fastest
- 2-cut is reasonable
- 3-cut is unpredictable
- Elitism ON + too many cuts slows everything down
- Bitwise mutation helps recover diversity

---

# **Elitism Effects**

![elitism_effect.png](attachment:45cea69c-e1fe-4cb0-8ec1-8a10ad995117:elitism_effect.png)

| Elitism | Behavior |
| --- | --- |
| **OFF** | Faster exploration, more 0-generation solves, but a few failures |
| **ON** | More stable, fewer failures, but slower average convergence |

Elitism is good when mutation is *low*, but harmful when mutation is *high* (over-exploitation).

---

# **Mutation Type Comparison**

![multi_cut_performance.png](attachment:d0f302f3-2f2c-438a-9b03-2c05fd0e0321:multi_cut_performance.png)

### **Swap Mutation**

- Produces the **fastest solutions**
- Strong for CutFill and PMX
- Ideal for permutation problems

### **Bitwise Mutation**

- More chaotic but **better at exploring**
- Helps Multi-cut avoid stagnation
- Slower but robust

---

# **Mutation Probability Comparison**

| Mutation Rate | Behavior |
| --- | --- |
| **0.2** | Risk of stagnation, especially without elitism |
| **0.5** | Best balance — stable convergence |
| **1.0** | Very fast early convergence, but sometimes unstable |

Interestingly, high mutation (1.0) + PMX is unexpectedly strong.

---

# **Exploration vs Exploitation**

### **Exploration Sources**

- Mutation probability 0.5–1.0
- Swap mutation (random exchanges)
- Multi-cut crossover (especially 2–3 cuts)
- Crossover probability 1.0

### **Exploitation Sources**

- PMX crossover (preserves mapping)
- Elitism
- CutFill when diversity is low

The best-performing configurations effectively **start exploratory** and naturally **shift toward exploitation** as fitness improves.

---

# **Conclusions**

- **PMX remains the most reliable crossover method**
- **Swap mutation dramatically improves convergence speeds**
- **Multi-cut is unpredictable but useful for exploration**
- **Elitism helps stability but can slow convergence**
- **Mutation rates ≥ 0.5 provide best performance**

The GA solved almost all configurations, achieving high reliability and demonstrating how crossover structure, mutation diversity, and elitist pressure interact in permutation-based optimization.

---