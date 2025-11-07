import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass(frozen=True)
class Config:
    population_size: int = int(os.getenv("POPULATION_SIZE", 100))
    parent_selection_count: int = int(os.getenv("PARENT_SELECTION_COUNT", 5))
    ga_pipeline_rounds: int = int(os.getenv("GA_PIPELINE_ROUNDS", 1000))
    max_evaluations: int = int(os.getenv("MAX_EVALUATIONS", 10000))
    n_queens: int = int(os.getenv("N_QUEENS", 8))
    mutation_probability: float = float(os.getenv("MUTATION_PROBABILITY", 0.5))
    crossover_probability: float = float(os.getenv("CROSSOVER_PROBABILITY", 1.0))
    mutation_type: str = os.getenv("MUTATION_TYPE", "swap")


CONFIG = Config()