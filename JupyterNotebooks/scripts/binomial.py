from scipy.special import comb
from matplotlib import pyplot as plt
import numpy as np

p_heads = np.linspace(0., 1., 100)

def binomial(p_heads, N_trials=10, n_heads=6):
    '''Calculate binomial distribution given the relevant parameters.'''
    return comb(N_trials, n_heads) * p_heads**n_heads * (1-p_heads)**(N_trials - n_heads)

N_trials = 10
n_heads = [6, 5, 4]

prob = binomial(p_heads, N_trials=N_trials, n_heads=n_heads[0]) * \
       binomial(p_heads, N_trials=N_trials, n_heads=n_heads[1]) * \
	   binomial(p_heads, N_trials=N_trials, n_heads=n_heads[2])

fig, ax = plt.subplots(1,1)
ax.plot(p_heads, prob)
ax.grid(1)
ax.set_xlabel('Coin Bias')
ax.set_ylabel('Probability')
fig.savefig('comb_binomial.png')



