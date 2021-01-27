#! /usr/bin/env python
import random
import threading
import math
import time

lock = threading.Lock()

def divideList(A, count):
    lists = []
    size = math.ceil(len(A)/count)

    for i in range(0, len(A), size):
        lists.append(A[i:i+size])

    return lists


def histCalc(A, histogram={}):

    for i in range(len(A)):
        lock.acquire()

        if histogram.get(A[i]) == None: 
            histogram[A[i]] = 1
        else:
            histogram[A[i]] += 1

        lock.release()

    return histogram

def histCalcMultithreading(A, noThreads=2):
    threads = []
    histogram = {}
    lists = divideList(A, noThreads)

    for i in range(noThreads):
        threads.append(threading.Thread(target=histCalc, args=(lists[i], histogram)))
    
    for i in range(noThreads):
        threads[i].start()

    return histogram

dim = 1000
matrix = [random.randint(0, 10)for e in range(dim)]

timestamp = time.perf_counter()
noThreads = 2

print("Histogram")
print(histCalcMultithreading(matrix,noThreads))
print("{0} threads - time: {1}".format(noThreads, (time.perf_counter()-timestamp)))

timestamp = time.perf_counter()
noThreads = 4

print("Histogram")
print(histCalcMultithreading(matrix,noThreads))
print("{0} threads - time: {1}".format(noThreads, (time.perf_counter()-timestamp)))

