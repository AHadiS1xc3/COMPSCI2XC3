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

#------------------------bubble sort---------------------------
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

#------------------------bubble sort2---------------------------
def bubble_sort2(L):
    for i in range(len(L)):
        #se a flage to track if any change is made
        flag=False
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                flag=True
                val = L[j+1]
                k = j 
                # find the better position to insert instead of a single swap.
                while k >= 0 and L[k] > val:
                    L[k+1] = L[k]
                    k -= 1
                L[k+1] = val  
        # if no change made, then list already sorted, return
        if flag == False:
            return
    return

#---------------------selection sort----------------------------
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
    
#-----------------------selection sort2--------------------------
def selection_sort2(L):
    for i in range (len(L)//2):
        min_val = L[i]
        max_val = L[i]
        min_index = i
        max_index = i
        for j in range(i, len(L)-i, 1):
            if (L[j] > max_val):
                max_val = L[j]
                max_index = j
            elif (L[j] < min_val):
                min_val = L[j]
                min_index = j
        # swap the min to the right place. 
        swap(L,i,min_index)
        # if we swaped max value with min_i before, then max value is at min_i now, we need to check and swap back.
        if (L[min_index] == max_val):
            swap(L,min_index,len(L)-i-1)
        else:
            swap(L,max_index,len(L)-i-1)
            
            
#---------------------test function-----------------------------

#----------------------bubble sort test sunction----------------

#---------------------random list---------------------------
def bubble_sort_test_random(n,trials):
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
    
def bubble_sort2_test_random(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            bubble_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;

#---------------------near sorted list---------------------------
def bubble_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def bubble_sort2_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            bubble_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
#---------------------reversed sorted list---------------------------
def bubble_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def bubble_sort2_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            bubble_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
#---------------------Sorted list---------------------------
def bubble_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def bubble_sort2_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            bubble_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    

#----------------------selection sort test sunction----------------
#---------------------random list---------------------------
def selection_sort_test_random(n,trials):
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
    
def selection_sort2_test_random(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_random_list(i,100)
            start = timeit.default_timer()
            selection_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
#---------------------near sorted list----------------------
def selection_sort_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def selection_sort2_test_near(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,i//4)
            start = timeit.default_timer()
            selection_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
#-------------------reversed sorted list---------------------
def selection_sort_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def selection_sort2_test_reversed(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_reversed_sorted_list(i,100)
            start = timeit.default_timer()
            selection_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
#--------------------sorted list---------------------------
def selection_sort_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
def selection_sort2_test_sorted(n,trials):
    t = []
    for i in range(1,n):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(i,100,0)
            start = timeit.default_timer()
            selection_sort2(L)
            end = timeit.default_timer()
            time += end - start 
        t.append(time/trials)
    return t;
    
#---------------------plot------------------------------

#---------------------bubble sort plot------------------

#----------------------random list----------------------
plot.figure("figure 2.1")
plot.plot(bubble_sort_test_random(500,10),label="bubble sort")
plot.plot(bubble_sort2_test_random(500,10),label="bubble sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Bubble sort (random list)")
plot.legend()
plot.show()
#----------------------near sorted list----------------------
plot.figure("figure 2.2")
plot.plot(bubble_sort_test_near(500,10),label="bubble sort")
plot.plot(bubble_sort2_test_near(500,10),label="bubble sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Bubble sort (near sorted list)")
plot.legend()
plot.show()
#----------------------reverded sorted list----------------------
plot.figure("figure 2.3")
plot.plot(bubble_sort_test_reversed(500,10),label="bubble sort")
plot.plot(bubble_sort2_test_reversed(500,10),label="bubble sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Bubble sort (reversed list)")
plot.legend()
plot.show()
#----------------------sorted list------------------------------
plot.figure("figure 2.4")
plot.plot(bubble_sort_test_sorted(500,10),label="bubble sort")
plot.plot(bubble_sort2_test_sorted(500,10),label="bubble sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Bubble sort (sorted list)")
plot.legend()
plot.show()

#---------------------selection sort plot------------------

#----------------------random list---------------------------
plot.figure("figure 2.5")
plot.plot(selection_sort_test_random(500,10),label="selection sort")
plot.plot(selection_sort2_test_random(500,10),label="selection sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Selection sort (random list)")
plot.legend()
plot.show()
#----------------------near sorted list----------------------
plot.figure("figure 2.6")
plot.plot(selection_sort_test_near(500,10),label="selection sort")
plot.plot(selection_sort2_test_near(500,10),label="selection sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Selection sort (near sorted list)")
plot.legend()
plot.show()
#---------------------reversed sorted list----------------------
plot.figure("figure 2.7")
plot.plot(selection_sort_test_reversed(500,10),label="selection sort")
plot.plot(selection_sort2_test_reversed(500,10),label="selection sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Selection sort (reversed list)")
plot.legend()
plot.show()

#----------------------sorted list---------------------------
plot.figure("figure 2.8")
plot.plot(selection_sort_test_sorted(500,10),label="selection sort")
plot.plot(selection_sort2_test_sorted(500,10),label="selection sort2")
plot.xlabel("list length")
plot.ylabel("time")
plot.title("Selection sort (sorted list)")
plot.legend()
plot.show()
