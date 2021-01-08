import os

def strucutre(a, b):
    i = os.listdir(a)
    for element in i:
        path = os.path.join(a, element)
        print(b * "   " + element)

strucutre(os.path.dirname(os.path.realpath(__file__)), 0)