"""Class for running optimization experiments using Random Hill Climbing (RHC), including grid search functionality."""

# Authors: Andrew Rollings (modified by Kyle Nakamura)
# License: BSD 3-clause

import mlrose_ky
from mlrose_ky.decorators import short_name

from mlrose_ky.runners._runner_base import _RunnerBase

"""
Example usage:

    experiment_name = 'example_experiment'
    problem = TSPGenerator.generate(seed=SEED, number_of_cities=22)

    rhc = RHCRunner(problem=problem,
                    experiment_name=experiment_name,
                    output_directory=OUTPUT_DIRECTORY,
                    seed=SEED,
                    iteration_list=2 ** np.arange(10),
                    max_attempts=5000,
                    restart_list=[25, 75, 100])   

    # the two data frames will contain the results
    df_run_stats, df_run_curves = rhc.run()               
"""


@short_name("rhc")
class RHCRunner(_RunnerBase):

    def __init__(self, problem, experiment_name, seed, iteration_list, restart_list, max_attempts=500, generate_curves=True, **kwargs):
        super().__init__(
            problem=problem,
            experiment_name=experiment_name,
            seed=seed,
            iteration_list=iteration_list,
            max_attempts=max_attempts,
            generate_curves=generate_curves,
            **kwargs,
        )
        self.restart_list = restart_list

    def run(self):
        return super().run_experiment(algorithm=mlrose_ky.random_hill_climb, restarts=("Restarts", self.restart_list))
