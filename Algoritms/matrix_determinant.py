import random
import numpy as np
tab = []

n = 2
for i in range(n):
    tab.append([])
    for j in range(n):
        x = random.randint(1,50)
        tab[i].append(x)

determ = np.linalg.det(tab)
print(determ)