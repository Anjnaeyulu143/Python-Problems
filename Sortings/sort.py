# def merge_two_sorted_arr(left_arr,right_arr,num_arr):
    
#     l_left_arr = len(left_arr)
#     l_right_arr = len(right_arr)
    
    
#     i = j = k = 0
    
#     while (i < l_left_arr and j < l_right_arr):
        
#         if (left_arr[i] <= right_arr[j]):
#             num_arr[k] = left_arr[i]
#             i += 1
#         else:
#             num_arr[k] = right_arr[j]
#             j += 1
            
#         k += 1
    
#     while (i < l_left_arr):
#         num_arr[k] = left_arr[i]
#         i += 1
#         k += 1
        
#     while (j < l_right_arr):
#         num_arr[k] = right_arr[j]
#         j += 1
#         k += 1

# def merge_sort(nums_arr):
    
#     # base condition if length of nums_arr is eaqual to 1
    
#     if (len(nums_arr) <= 1):
#         return
    
#     mid = len(nums_arr)//2
    
#     left_arr = nums_arr[:mid]
#     right_arr = nums_arr[mid:]
    
#     merge_sort(left_arr)
    
#     merge_sort(right_arr)
    
    
#     merge_two_sorted_arr(left_arr,right_arr,nums_arr)
    


# if __name__=='__main__':
#     nums_list = [10,9,11,25,20]
#     merge_sort(nums_list)
#     print(nums_list)

def insertion_sort(nums_arr):
    
    n = len(nums_arr)
    
    for i in range (1,n):
        
        temp = nums_arr[i]
        
        a = -1
        
        for j in range (i-1,-1,-1):
            if nums_arr[j] > temp:
                val = nums_arr[j]
                nums_arr[j+1] = val 
            elif nums_arr[j] < temp:  
                a = j
                break
        
        nums_arr[a+1] = temp
            
            
    return nums_arr
        



if __name__ == '__main__':
    nums_list = [4,2,1]
    result = insertion_sort(nums_list)
    print(result)



