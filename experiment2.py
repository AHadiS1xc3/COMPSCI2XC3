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

#------------------------bad bubble sort-------------------------
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

#------------------------bubble sort2----------------------------
'''def bubble_sort2(L):
    position=len(L)
    for i in range(position):
        flag = False
        for j in range(0,position-1):
            if L[j] > L[j+1]:
                position = j+1
                swap(L, j, j+1)
                flag = True
        if flag == False:
            return L
        i = position
    return L
'''

def bubble_sort2(L):
    for i in range(len(L)):
        flag=False
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                flag=True
                val = L[j+1]
                k = j 
                while k >= 0 and L[k] > val:
                    L[k+1] = L[k]
                    k -= 1
                L[k+1] = val       
        if flag == False:
            return
    return
    

#---------------------bad selection sort-------------------------
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
        min_i = i
        max_i = i
        for j in range(i, len(L)-i, 1):
            if (L[j] > L[max_i]):
                max_val = L[j]
                max_i = j
            elif (L[j] < L[min_i]):
                min_val = L[j]
                min_i = j
        # swap the min to the right place. 
        swap(L,i,min_i)
        ## if we swaped max value with min_i before, then max value is at min_i now, we need to check and swap back.
        if (L[min_i] == max_val):
            swap(L,min_i,len(L)-i-1)
        else:
            swap(L,max_i,len(L)-i-1)

'''def selection_sort2(L):
    for i in range (len(L)//2):
        min_max=find_max_min_index(L,i,len(L)-i)
        min_i = min_max[0]
        max_i = min_max[1]
        max_val=min_max[2]
        # swap the min to the right place. 
        
        swap(L,i,min_i)
 
        ## if we swaped max value with min_i before, then max value is at min_i now, we need to check and swap back. 
        if (L[min_i] == max_val):
            swap(L,min_i,len(L)-i-1)
        else:
            swap(L,max_i,len(L)-i-1)
    return L
    
def find_max_min_index(L, left,right):
    min_val = L[left]
    max_val = L[left]
    min_i = left
    max_i = left
    for i in range(left, right, 1):
            if (L[i] > L[max_i]):
                max_val = L[i]
                max_i = i
            elif (L[i] < L[min_i]):
                min_val = L[i]
                min_i = i
    return [min_i,max_i,max_val]
'''

#---------------------test function-------------------------
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
    
def bubble_sort2_test(n,trials):
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

def selection_sort_test(n,trials):
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
    
def selection_sort2_test(n,trials):
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
    

#---------------------plot-------------------------
arr=[[1, 2, 3, 4], [1, 2 ,4, 3], [2, 1, 3, 4],[2, 1, 4, 3] ,[1, 2, 0, 1], [1, 2, 1, 0], [2, 1, 0, 1],[2, 1, 1, 0],[3, 4, 2, 1],                           
[3, 4, 1, 2],[4, 3, 2, 1],[4, 3, 1, 2],[1, 1, 1, 1]]


plot.rcParams["figure.figsize"] = (13,5)
plot.figure()

plot.subplot(1,2,1)
plot.plot(bubble_sort_test(500,10),label="bubble sort")
plot.plot(bubble_sort2_test(500,10),label="bubble sort2")
plot.legend()

plot.subplot(1,2,2)
plot.plot(selection_sort_test(500,10),label="selection sort")
plot.plot(selection_sort2_test(500,10),label="selection sort2")
plot.legend()

plot.show()

'''
selection_sort2 compare to old one
1. max, min same time, reduce the swaps
2. loop boundaries should updated, reduced the checking length
3. did not use find_min, and did not create a seperate find_min_max, 
because it would increase the function call(need call find_min_max many times).
4. use min_val and max_val to store the current min/max value, instead of directly using L[min_i] and L[max_i]. 
It reduce many array accessing which saves a lot of time, but may increase the memory space used. 

'''

'''
bubble_sort2 compare to old one
1. create a flag, if no swap for one iteration at all, means already sorted, then return. 
2. reduce swap by finding the better position to fit, move elements one by one, then insert to the position. 


quesions: 
naming for bubblesort2()/bubble_sort2()?

An explicit outline of the experiments you ran. That is, list length values, how many “runs”?

1. The experiments we did is sorting the list using the corresponding sorting algorithms with list length from 1 to 500, 
for each length we create new random list 20 times and sort to take the average. So the result will be more accurate . 
'''
