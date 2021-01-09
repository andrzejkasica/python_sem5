import random
tab1 = []
tab2 = []
mult = []

for i in range(128):
    tab1.append([])
    tab2.append([])
    for j in range(128):
        x = random.randint(1,50)
        tab1[i].append(x)
        x = random.randint(1,50)
        tab2[i].append(x)

for i in range(0,8):
    mult.append([])
    for j in range(0,8):
           mult[i].append(0)
           
for i in range(0,8):
    for j in range(0,8):
        for k in range(0,8):
            mult[i][j] += tab1[i][k] * tab2[k][j]


