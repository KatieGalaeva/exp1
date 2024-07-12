import numpy as np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed


initial_balance = 15000
bet = 1000

balance = initial_balance
balances = [balance]
number_bets=[]

def simulate(balance, bet, random_coef):
    count=0        
    while count<1000000 and balance>0:
        coef=random_coef()
        for i in range(len(coef)):
            if coef[i]==0:
                balance-=bet
            if coef[i]==0.5:
                balance-=coef[i]*bet
            else:
                balance+=coef[i]*bet
            balances.append(balance)
            count+=1
            if bet>balance:    
                break
        if bet>balance:  
            break
    number_bets.append(count)    

        
    return number_bets
def random_coef():
    coef=np.random.choice([15, 7, 5, 4, 3, 2.5, 2, 1.7, 1.5, 1.2, 0.5, 0], 1000000, p=[3.3333333333333335e-05, 0.0004166666666666667, 0.0025, 0.015, 0.018333333333333334, 0.025, 0.035, 0.04333333333333334, 0.04333333333333333, 0.12333333333333332, 0.3333333333333333, 0.3603833333])
    d_coef={}
    for i in coef:
        d_coef[i]=1+d_coef.get(i,0)
    sorted_d_coef=sorted(d_coef.items(), key=lambda kv: kv[0])
    return coef

for epoch in range(10):
    number_bets=simulate(balance, bet, random_coef)
print(np.mean(number_bets))

N_CORES = 12 # количество задействованных ядер процессора

list_array = np.array_split(bigdata, N_CORES)
data = Parallel(n_jobs=N_CORES, verbose=10)(delayed(lambda array: list(map(bogosort, array)))(array) for array in list_array)
