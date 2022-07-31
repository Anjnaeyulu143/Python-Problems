# Merge Sort T.C O(nlog n)

def merge_two_sorted_lists(left_arr,right_arr,nums_arr):
    
    # Finding the length of the two arrays
    
    l_left_arr = len(left_arr)
    l_right_arr = len(right_arr)
    
    
    
    i = j = k = 0
    
    while ((i < l_left_arr) and (j < l_right_arr)):
        
        if (left_arr[i] < right_arr[j]):
            nums_arr[k] = left_arr[i]
            i += 1
        else:
            nums_arr[k] = right_arr[j]
            j += 1
        
        k += 1
            
    while(i < l_left_arr):
        nums_arr[k] = left_arr[i]
        i += 1
        k += 1
    
    
    while(j < l_right_arr):
        nums_arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(nums_arr):
    
    if (len(nums_arr) <= 1):
        return
    
    # Finding the mid index
    
    mid_index = len(nums_arr)//2
    
    
    left_arr = nums_arr[:mid_index]
    right_arr = nums_arr[mid_index:]
    
    # Applying recurrsion for left array until it returns single element
    
    merge_sort(left_arr)
    
    # Applying recurrsion for right array until it returns single element
    
    merge_sort(right_arr)
    
    merge_two_sorted_lists(left_arr,right_arr,nums_arr)
    
    

if __name__ == '__main__':
    
    nums_list = [1,2,3,4,5,6,7]
    merge_sort(nums_list)
    print(nums_list)