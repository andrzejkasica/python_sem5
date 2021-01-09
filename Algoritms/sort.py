import random

tab = []
for i in range(0,50):
    x = random.randint(1,100)
    tab.append(x)

for i in range(len(tab) - 1):
    for j in range(0, len(tab) - i - 1):
        if tab[j] > tab[j + 1]:
            tab[j], tab[j + 1] = tab[j + 1], tab[j]

print("własna: ",tab)

tab.sort()


print("sort: ",tab)