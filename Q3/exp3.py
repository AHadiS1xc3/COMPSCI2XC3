"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import timeit
import random
import matplotlib.pyplot as plt
import math as m 


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



# ******************* Experiment 3  *******************
# DEFAULTS vals
# len_lst = 5000
# max = 1000
# num_exps = int (len_lst*m.log(len_lst)//2)
# Note running this code with DEFAULT vals will  take approximately 6 mins
# These are the values used to create Fig 3.1



len_lst = 5000
max = 1000
num_exps = int (len_lst*m.log(len_lst)//2)

print("NUM EXPS: ", num_exps)

# This scale variable smooths our graph by incrementing 
# the number of swaps at a constant rate at each iteration 
scale        = 500
bub_times    = []
ins_times    = []
select_times = []


for i in range (0, num_exps, scale):
    lst = create_near_sorted_list(len_lst,max,i)
    
    idx = i // scale
    print("I val: " ,i , "IDX: " , idx )
    lst_copy = lst.copy()
    start = timeit.default_timer()
    bubble_sort(lst_copy)
    end   = timeit.default_timer()
    bub_times.append (end - start)

    lst_copy = lst.copy()
    start = timeit.default_timer()
    insertion_sort(lst_copy)

    end   = timeit.default_timer()
    ins_times.append (end - start)


    lst_copy = lst.copy()
    start = timeit.default_timer()
    selection_sort(lst_copy)
    end   = timeit.default_timer()
    select_times.append (end - start)







l1  = range(0,num_exps,scale)
plt.plot( l1 , bub_times, label="Bubble sort")
plt.plot( l1 , select_times, label= "Selection sort")
plt.plot( l1 , ins_times, label= "Insertion sort")

plt.legend(loc = "upper right")
plt.title ('Swaps vs time')
plt.xlabel('Swaps')
plt.ylabel('time in seconds')
plt.show()


"""
plt.plot(select_times)
plt.show()

plt.plot(ins_times)
plt.show()
"""










