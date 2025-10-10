import numpy as np
from numpy import inf

# Given distance matrix
d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
], dtype=float)

iteration = 100
n_ants = 5
n_citys = 5

# Initialization
m = n_ants
n = n_citys
e = 0.5       # evaporation rate
alpha = 1     # pheromone factor
beta = 2      # visibility factor

# Calculate visibility (1/d), avoiding divide by zero
visibility = np.zeros_like(d)
with np.errstate(divide='ignore', invalid='ignore'):
    visibility = 1 / np.where(d != 0, d, inf)
visibility[~np.isfinite(visibility)] = 0  # replace inf with 0

# Initial pheromone levels
pheromone = 0.1 * np.ones((n, n))

# Initialize routes of the ants
rute = np.ones((m, n + 1))

for ite in range(iteration):
    rute[:, 0] = 1  # all ants start at city 1

    for i in range(m):
        temp_visibility = np.array(visibility)

        for j in range(n - 1):
            cur_loc = int(rute[i, j] - 1)
            temp_visibility[:, cur_loc] = 0

            p_feature = np.power(pheromone[cur_loc, :], alpha)
            v_feature = np.power(temp_visibility[cur_loc, :], beta)
            combine_feature = p_feature * v_feature
            total = np.sum(combine_feature)

            probs = combine_feature / total if total != 0 else np.zeros_like(combine_feature)
            cum_prob = np.cumsum(probs)

            r = np.random.random_sample()
            city = np.nonzero(cum_prob > r)[0][0] + 1
            rute[i, j + 1] = city

        # Find remaining city and complete the route
        left = list(set(range(1, n + 1)) - set(rute[i, :-2]))[0]
        rute[i, -2] = left

    rute_opt = np.array(rute)
    dist_cost = np.zeros((m, 1))

    # Calculate distance of each route
    for i in range(m):
        s = 0
        for j in range(n - 1):
            s += d[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1]
        dist_cost[i] = s

    # Find best route
    dist_min_loc = np.argmin(dist_cost)
    dist_min_cost = float(dist_cost[dist_min_loc])  # FIXED deprecation warning
    best_route = rute[dist_min_loc, :]

    # Pheromone evaporation
    pheromone = (1 - e) * pheromone

    # Update pheromone
    for i in range(m):
        for j in range(n - 1):
            dt = 1 / dist_cost[i]
            a = int(rute_opt[i, j]) - 1
            b = int(rute_opt[i, j + 1]) - 1
            pheromone[a, b] += dt

print('Route of all the ants at the end:')
print(rute_opt)
print()
print('Best path:', best_route)
print('Cost of the best path:', int(dist_min_cost) + int(d[int(best_route[-2]) - 1, 0]))
