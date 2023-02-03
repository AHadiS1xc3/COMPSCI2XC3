import timeit
import random
import matplotlib.pyplot as plot

def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L
    
def create_reversed_sorted_list(length,max_value):
    L = create_random_list(length, max_value)
    L.sort()
    L.reverse()
    return L
    
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

# *************************************
            
# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# ------------------test function-----------------------
#---------------------random list---------------------------
def insertion_sort_test_random(n,trials):
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

def merge_sort_test_random(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            mergesort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def quick_sort_test_random(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

#---------------------near sorted list list---------------------------
def insertion_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def merge_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            mergesort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def quick_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

#---------------------reversed sorted list---------------------------
def insertion_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def merge_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            mergesort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def quick_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
#---------------------Sorted list---------------------------
def insertion_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

def merge_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            mergesort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def quick_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

#---------------------plot------------------------------
#----------------------random list(length 100)----------------------

plot.figure("figure 8.1")
plot.plot(insertion_sort_test_random(100,10),label="insertion sort")
plot.plot(merge_sort_test_random(100,10),label="merge sort sort")
plot.plot(quick_sort_test_random(100,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("random list (length 100)")
plot.legend()
plot.show()

#----------------------random list(length 60)----------------------

plot.figure("figure 8.2")
plot.plot(insertion_sort_test_random(60,10),label="insertion sort")
plot.plot(merge_sort_test_random(60,10),label="merge sort sort")
plot.plot(quick_sort_test_random(60,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("random list (length 60)")
plot.legend()
plot.show()

#----------------------near sorted list(length 100)----------------------
plot.figure("figure 8.3")
plot.plot(insertion_sort_test_near(100,10),label="insertion sort")
plot.plot(merge_sort_test_near(100,10),label="merge sort sort")
plot.plot(quick_sort_test_near(100,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("near sorted list (length 100)")
plot.legend()
plot.show()

#----------------------near sorted list(length 150)----------------------
plot.figure("figure 8.4")
plot.plot(insertion_sort_test_near(150,10),label="insertion sort")
plot.plot(merge_sort_test_near(150,10),label="merge sort sort")
plot.plot(quick_sort_test_near(150,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("near sorted list (length 150)")
plot.legend()
plot.show()

#----------------------reverded sorted list(length 100)----------------------

plot.figure("figure 8.5")
plot.plot(insertion_sort_test_reversed(100,10),label="insertion sort")
plot.plot(merge_sort_test_reversed(100,10),label="merge sort sort")
plot.plot(quick_sort_test_reversed(100,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("reversed list (length 100)")
plot.legend()
plot.show()

#----------------------reverded sorted list(length 30)----------------------

plot.figure("figure 8.6")
plot.plot(insertion_sort_test_reversed(30,10),label="insertion sort")
plot.plot(merge_sort_test_reversed(30,10),label="merge sort sort")
plot.plot(quick_sort_test_reversed(30,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("reversed list (length 30)")
plot.legend()
plot.show()

#----------------------sorted list (length 100)------------------------------

plot.figure("figure 8.7")
plot.plot(insertion_sort_test_sorted(100,10),label="insertion sort")
plot.plot(merge_sort_test_sorted(100,10),label="merge sort sort")
plot.plot(quick_sort_test_sorted(100,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Sorted list (length 100)")
plot.legend()
plot.show()

#----------------------sorted list (length 500)------------------------------

plot.figure("figure 8.7")
plot.plot(insertion_sort_test_sorted(500,10),label="insertion sort")
plot.plot(merge_sort_test_sorted(500,10),label="merge sort sort")
plot.plot(quick_sort_test_sorted(500,10),label="quick sort")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Sorted list (length 500)")
plot.legend()
plot.show()