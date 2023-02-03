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
    
 
def dual_quicksort(L):
    return dual_quicksort_copy(L)

'''def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
  '''  
def dual_quicksort_copy(L):
    if len(L) <= 2:
        return L
    if(L[1]<L[0]):
        L[0], L[1]=L[1],L[0]
        
    pivot1, pivot2 = L[0], L[1]
    left,middle,right = [],[],[]
    
    for num in L[2:]:
        if num < pivot1:
            left.append(num)
        elif pivot1 <=num <=pivot2 :
            middle.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot1]+ quicksort_copy(middle)+[pivot2] + quicksort_copy(right)
     
   
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
    
def dual_quick_sort_test_random(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            dual_quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t

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
    
def dual_quick_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            dual_quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t

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
    
def dual_quick_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            dual_quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t
    
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
    
def dual_quick_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            dual_quicksort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t

#----------------------random list----------------------

plot.figure("figure 6.1")
plot.plot(quick_sort_test_random(500,10),label="quick sort")
plot.plot(dual_quick_sort_test_random(500,10),label="dual quick sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("random list")
plot.legend()
plot.show()

#----------------------near sorted----------------------
plot.figure("figure 6.2")
plot.plot(quick_sort_test_near(500,10),label="quick sort")
plot.plot(dual_quick_sort_test_near(500,10),label="dual quick sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("near sorted list")
plot.legend()
plot.show()

#----------------------reverded sorted list ----------------------
plot.figure("figure 6.3")
plot.plot(quick_sort_test_reversed(500,10),label="quick sort")
plot.plot(dual_quick_sort_test_reversed(500,10),label="dual quick sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("reversed list")
plot.legend()
plot.show()

#----------------------sorted list------------------------------
plot.figure("figure 6.4")
plot.plot(quick_sort_test_sorted(500,10),label="quick sort")
plot.plot(dual_quick_sort_test_sorted(500,10),label="dual quick sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("sorted list")
plot.legend()
plot.show()