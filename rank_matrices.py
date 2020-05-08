"""
(Ranks of random matrices) Generate square (n x n) matrices with random entries (for instance Gaussian or uniform
random entries). For each n belonging to {10,20,30,40,50}, run 100 trials and report the statistics of the rank of
the matrix generated for each trial (mean, median, min, max). What do you notice? Please turn in the code you used to
produce the data.
"""

import numpy as np

def answer(n):
    # Dictionary to store the statistics of the matrices
    stats = {'rank': list(),
             'mean': list(),
             'median': list(),
             'min': list(),
             'max': list()}
    for i in range(100):
        # random generated square matrix
        matrix = np.random.rand(n, n)
        # appending the required statistics to the dictionary
        stats['rank'].append(np.linalg.matrix_rank(matrix))
        stats['mean'].append(np.mean(matrix))
        stats['median'].append(np.median(matrix))
        stats['min'].append(matrix.min())
        stats['max'].append(matrix.max())
    # returning a tuple of the mean value of required statistics
    return (np.mean(stats['rank']), np.mean(stats['mean']),
            np.mean(stats['median']), np.mean(stats['min']),
            np.mean(stats['max'])), stats

# different dimensions for the matrices
set_of_ns = [10,20,30,40,50]
# dictionary to append statistics for each n
answer_dict = {n : None for n in set_of_ns}

for n in set_of_ns:
    avg_stats, stats = answer(n)
    intermediate_dict = {'avg': avg_stats,
                         'stats': stats}
    answer_dict[n] = intermediate_dict

for key, val in answer_dict.items():
    avg = val['avg']
    print('key :', key, '-- ', avg)

