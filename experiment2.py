import timeit
import random
import matplotlib.pyplot as plot


def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L
    
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]
    
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


def insertionSort(L):
    if (n := len(L)) <= 1:
      return
    for i in range(1, n):
         
        key = L[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < L[j] :
                L[j+1] = L[j]
                j -= 1
        L[j+1] = key
        
def bubble_sort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def insertionSort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            insertionSort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;


plot.plot(bubble_sort_test(500,1), label ="bubble sort")
plot.plot(insertionSort_test(500,1),label="insertion sort")
plot.legend()
plot.show()

