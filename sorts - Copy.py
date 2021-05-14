import random 
import time
import math


def bubble_sort(my_list):       
    # do n passes on the list
    swapped = True
    while swapped:
       swapped = False   

	   # check neighbours and swap them if needed     
       for j in range(len(my_list)-1):
           if my_list[j] > my_list[j+1]:
               temp = my_list[j]
               my_list[j] = my_list[j+1]
               my_list[j+1] = temp     
               swapped = True


def selection_sort(my_list):  
    for i in range(len(my_list)-1): # perform n-1 passes
        
    	# find the minimum in the unsorted part of my_list 
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j]< my_list[min_index]:
                min_index = j
            
        # swap this min element with the first unsorted element from my_list 
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp 


def insertion_sort(my_list):
    i = 1                   # i is the size of the sorted list
    while i < len(my_list): # while the list is not sorted yet
    	j = i
    
    	# place the element j at the proper place in the sorted list
    	while j > 0 and my_list[j-1] > my_list[j]:
    	  # swap 
    	  temp = my_list[j]
    	  my_list[j] = my_list[j-1]
    	  my_list[j-1] = temp
    	  j = j - 1 
            
    	i = i + 1


def merge_sort(my_list):
    # if the list is empty or contains just one element, no need to sort 
    if len(my_list) <= 1: return my_list
     
    # we divide the work in two halves, and sort them recursively
    mid = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid])      
    right = merge_sort(my_list[mid:])   
    
    # merge the two sorted halves, while keeping the list sorted
    my_sorted_list = []
    while left != [] or right != []: 
        if left == []: my_sorted_list.append(right.pop(0))  # left is empty
        elif right == []: my_sorted_list.append(left.pop(0)) # right is empty
        elif left[0] < right[0]: my_sorted_list.append(left.pop(0))
        else:  my_sorted_list.append(right.pop(0))
    
    return my_sorted_list


  
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:       
        length = len(lst)
        # randomly generate a pivot point # 
        idx = random.randint(0,length-1) 
        # create 3 list to store elements of lst #
        left = []
        equal = []
        right = []
        for item in lst:
            if item < lst[idx]:
                left.append(item)
            elif item > lst[idx]:
                right.append(item)
            else:
                equal.append(item)

        return quick_sort(left) + equal + quick_sort(right) 
        
    
def add_to_heap(heap,element):
    ## Add element to the heap first 
    heap.append(element)
    ## Find the index of element ## 
    idx = len(heap)-1
    ## Swapping with parent node while idx >= 0 ##
    ## To prevent out of index error ##
    while idx > 0:
        ## To find the parent node ## 
        parent_idx = math.ceil(idx/2) - 1 
       
        ## swap only if the element is smaller than the parent
        if heap[idx] < heap[parent_idx]:
            heap[idx],heap[parent_idx] = heap[parent_idx],heap[idx]
            idx = parent_idx 
        else:
            break
        
    
 
def remove_min_from_heap(heap):
    root = heap.pop(0)

    if heap == []:
        return None

    else:
        pass
    
    last = heap.pop(-1)
    heap.insert(0,last)
    ## index of your current root ## 
    idx = 0 
    while idx <= len(heap) -1:
        left = 2*idx + 1 
        right = 2*idx + 2
        is_left = left > len(heap) - 1 
        is_right = right > len(heap) - 1
        # only 1 child # 
        if not is_left and is_right: 
          if heap[idx] > heap[left]:
            heap[idx],heap[left] = heap[left],heap[idx]
          else:
            break 
        elif not is_right and is_left: 
          if heap[idx] > heap[right]:
            heap[idx],heap[right] = heap[right],heap[idx]
            idx = right 
          else:
            break 
        else:
          pass 

          
        if is_left and is_right:
            break
        else:
            pass

        
        if left > len(heap)-1 or right > len(heap)-1:
            break
        else:
            pass
        
        if heap[left] < heap[right]:
            child = heap[left]
            child_idx = left
        
        elif heap[right] < heap[left]:
            child = heap[right]
            child_idx = right
        
        elif heap[left] == heap[right]:
            child = heap[left]
            child_idx = left
        
        
        
        if heap[idx] > child:
            heap[idx],heap[child_idx] = heap[child_idx],heap[idx]
            idx = child_idx 
        
        else:
            break 
    
    return root 

                
                

            
# Output: [5,8,9,13,24,12,18,16,14,26,33,42]    

def heap_sort(my_list):
    ## sucessively add n elements to empty heap ## 
    empty = []
    sorted_lst = []
    for item in my_list:
        add_to_heap(empty,item)
        
    ## Iteratively Remove the root of empty and store in 
    ## sorted_lst 
    while len(empty) >= 1:
        sorted_lst.append(empty[0])
        remove_min_from_heap(empty)
    
    
    return sorted_lst 

## Test cases ## 

'''long_lst = [7, 16, 36, 14, 39, 5, 25, 17, 17, 31, 29, 1, 34, 7, 21, 28, 32, 40, 11, 36, 17, 40, 19, 12, 36, 32, 27, 29, 23, 39]
lst = [2,5,9,8,24,12,18,13,14,26,33,42,16]
empty = []
sorted_lst = []
for item in long_lst: 
    add_to_heap(empty,item)
print(empty)
pop = remove_min_from_heap(empty)
print(pop)'''

###



def test_sorting(algo,my_tab,display):
    tab = my_tab.copy()
    print("testing",algo,str(" "*(14-len(algo))),"... ",end='')
    t = time.time()
    temp = eval(algo + "(tab)")
    if temp != None: tab = temp
    print("done ! It took {:.2f} seconds".format(time.time() - t))
    if display: print(tab,end='\n\n')
    

print("\n ******** Testing to sort a small table of 30 elements ********")
NUMBER_OF_ELEMENTS = 30
tab = [random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)] 
#tab = list(set([random.randint(1, 40) for i in range(NUMBER_OF_ELEMENTS)]))
print("Original table: ")
print(tab,end='\n\n')
test_sorting("bubble_sort",tab,True)
test_sorting("selection_sort",tab,True)
test_sorting("insertion_sort",tab,True)
test_sorting("merge_sort",tab,True)
test_sorting("quick_sort",tab,True)
test_sorting("heap_sort",tab,True)

print("\n ******** Testing to sort a big table of 5000 elements ********")
NUMBER_OF_ELEMENTS = 5000
tab = list(set([random.random() for i in range(NUMBER_OF_ELEMENTS)]))
test_sorting("bubble_sort",tab,False)
test_sorting("selection_sort",tab,False)
test_sorting("insertion_sort",tab,False)
test_sorting("merge_sort",tab,False)
test_sorting("quick_sort",tab,False)
test_sorting("heap_sort",tab,False)
