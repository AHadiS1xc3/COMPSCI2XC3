"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import timeit
import random
import matplotlib.pyplot as plot


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# *********************************************Our Work ***********************
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
    
def insertionSort_test1(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def insertionSort_test2(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            insertion_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def selectionSort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;



plot.plot(bubble_sort_test(500,10), label ="bubble sort")
plot.plot(insertionSort_test1(500,10),label="insertion sort 1")
plot.plot(insertionSort_test2(500,10),label="insertion sort 2")
plot.plot(selectionSort_test(500,10),label="selection sort")
plot.legend()
plot.show() 

'''
def bubble_sort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, int(i/4))
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def insertionSort_test1(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, int(i/4))
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def insertionSort_test2(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, int(i/4))
            start = timeit.default_timer()
            insertion_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def selectionSort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, int(i/4))
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;  '''

'''
def bubble_sort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def insertionSort_test1(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def insertionSort_test2(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            insertion_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def selectionSort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;  '''

''' 
def bubble_sort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            L = list(reversed(L))
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def insertionSort_test1(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            L = list(reversed(L))
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def insertionSort_test2(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            L = list(reversed(L))
            insertion_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def selectionSort_test(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100, 0)
            start = timeit.default_timer()
            L = list(reversed(L))
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t; '''

plot.plot(bubble_sort_test(500,10), label ="bubble sort")
plot.plot(insertionSort_test1(500,10),label="insertion sort 1")
plot.plot(insertionSort_test2(500,10),label="insertion sort 2")
plot.plot(selectionSort_test(500,10),label="selection sort")
plot.legend()
plot.show()
