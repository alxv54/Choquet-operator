#essais capacity


import Capacity


t = CapacitySet.CapacitySet({frozenset(): 0, frozenset({'3', '2', '4', '1'}): 1, frozenset({'1'}): 0.1, frozenset({'2'}): 0.2, 
       frozenset({'3'}): 0.1, frozenset({'4'}): 0.3, frozenset({'3', '2'}): 0.7082259973350473, 
       frozenset({'3', '1'}): 0.7834792399805287, frozenset({'3', '4', '1'}): 0.9536303899863656, 
       frozenset({'3', '4'}): 0.6538741482956895, frozenset({'3', '2', '1'}): 0.8070513547828126, 
       frozenset({'4', '1'}): 0.3, frozenset({'2', '4'}): 0.32535600340934057, 
       frozenset({'3', '2', '4'}): 0.7394800676114206, frozenset({'2', '4', '1'}): 0.5, 
       frozenset({'2', '1'}): 0.4297823119322727})


for i in range(2**t.N):
       print(f'a={t.subsets(i):s}, b={t.mu(t.subsets(i)):d}')

