
"""
Part1
BO used in music volume preference
"""

!pip install GPy
!pip install GPyOpt
!pip install matplotlib==3.1.3

"""BO"""

import GPy
import GPyOpt
import numpy as np
import matplotlib.pyplot as plt

# objective function
def simulated_user_preference(volume):
    return -10 * np.exp(-0.5 * ((volume - 65)**2) / (2 * 10**2)) + np.random.normal(0, 0.5)

# BO
bounds = [{'name': 'volume', 'type': 'continuous', 'domain': (0, 100)}]
myBopt = GPyOpt.methods.BayesianOptimization(
    f=simulated_user_preference,
    domain=bounds,
    acquisition_type='EI',
    exact_feval=False,
    normalize_Y=False,
    initial_design_numdata=5
)
max_iter = 10

#run and plot
for i in range(max_iter):
    myBopt.run_optimization(max_iter=1, verbosity=False)
    myBopt.plot_acquisition()

# result
optimized_volume_level = myBopt.x_opt
optimized_user_preference_value = myBopt.fx_opt
print(f'preference volume: {optimized_volume_level}')
print(f'preference rating: {-optimized_user_preference_value}')

"""Part2

BO with experiment
"""

import numpy as np
import GPyOpt
from numpy.random import seed
import matplotlib.pyplot as plt

# rate
def f_u(volume):
    print(f"Volume: {volume[0][0]}")
    res = input("rate this volume(0 to 10): ")
    return -float(res)

# BO
def run_bo(max_iter):
    bounds = [{'name': 'volume', 'type': 'continuous', 'domain': (0, 100)}]
    myBopt = GPyOpt.methods.BayesianOptimization(
        f=f_u,
        domain=bounds,
        acquisition_type='EI',
        exact_feval=True,
        normalize_Y=False,
        initial_design_numdata=1,
    )

#test and show
    for i in range(max_iter):
        myBopt.run_optimization(max_iter=1, verbosity=False)
        myBopt.plot_acquisition()
    return myBopt

# main part
if __name__ == "__main__":
    seed(123)  # 设定随机种子
    n_iter = 10  # 设定迭代次数

    bo = run_bo(n_iter)
    bo_volume_levels, bo_satisfaction_scores = bo.get_evaluations()
    optimized_volume = bo.x_opt
    optimized_rating = -bo.fx_opt
    print(f'preference volume: {optimized_volume[0]}')
    print(f'preference volume rating: {optimized_rating}')
