import random
tab1 = []
tab2 = []
sum1 = []

for i in range(128):
    tab1.append([])
    tab2.append([])
    for j in range(128):
        x = random.randint(1,50)
        tab1[i].append(x)
        x = random.randint(1,50)
        tab2[i].append(x)

for i in range(128):
    sum1.append([])
    for j in range(128):
        sum1[i].append(tab1[i][j] + tab2[i][j])


