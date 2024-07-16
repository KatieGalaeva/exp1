from collections import defaultdict
import random
import numpy as np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed


def draw_random_multipliers(multipliers, n_samples):
    coeffs, prob = list(zip(*multipliers))
    return np.random.choice(coeffs, n_samples, p=prob)


def draw_random_bet(bet_values):
    return random.choice(bet_values)


def simulate(balance, multipliers, bet_values, n_iter):
    count = 0
    balance_history = []
    drawn_multipliers = draw_random_multipliers(multipliers, n_iter)
    for multiplier in drawn_multipliers:
        bet = draw_random_bet(bet_values)
        if multiplier==0:
            balance-=bet
        if multiplier==0.5:
            balance-=multiplier*bet
        else:
            balance+=multiplier*bet
        balance_history.append(balance)
        count+=1
        if balance <= 0:    
            break
        
    return count, balance_history


initial_balance = 15000
n_iter = 1000000
balances = [initial_balance]
bet_values=[500,1000,1500,2000,2500,3000]
multipliers=[
    (15, 3.3333333333333335e-05), 
    (7, 0.0004166666666666667), 
    (5, 0.0025), 
    (4, 0.015), 
    (3, 0.018333333333333334), 
    (2.5, 0.015), 
    (2, 0.025), 
    (1.7, 0.02833333333333334), 
    (1.5, 0.03833333333333333), 
    (1.2, 0.10333333333333332), 
    (0.5, 0.3333333333333333), 
    (0, 0.4203833333)
]

number_bets=[]
for epoch in range(20000):
    sim_count, sim_balance = simulate(initial_balance, multipliers, bet_values, n_iter)
    number_bets.append(sim_count)

print(np.mean(number_bets))
print(np.max(number_bets))
print(np.min(number_bets))
print("max balance", np.max(balances))
print(number_bets)
#python .\dragon\simulatiom.py


freq_bets=defaultdict(int)
for i in number_bets:
    freq_bets[i] += 1

sorted_freq_bets=sorted(freq_bets.items(), key=lambda kv: kv[0])

xs=[]
ys=[]
for freq_bet in sorted_freq_bets:
    xs.append(freq_bet[1])
    ys.append(freq_bet[0])

print(sorted_freq_bets)
plt.plot(ys,xs)
plt.show()

# N_CORES = 12 
# epoch=list(range(100))

# list_array = np.array_split(epoch, N_CORES)
# data = Parallel(n_jobs=N_CORES, verbose=10)(delayed()(array) for array in epoch)

# if __name__ == 'main':
