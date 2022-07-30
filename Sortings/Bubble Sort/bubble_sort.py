# Bubble Sort T.C is O(n) in best case && O(n2) in wrost case

def bubble_sort(nums_arr):
    
    n = len(nums_arr)
    
    for i in range(n-1):
        
        nums_arr_is_sorted = True
        
        for j in range(n-i-1):
            if (nums_arr[j] > nums_arr[j+1]):
                nums_arr[j],nums_arr[j+1] = nums_arr[j+1],nums_arr[j]
                nums_arr_is_sorted = False

        if (nums_arr_is_sorted):
            break
        
    return nums_arr

if __name__ == '__main__':

    nums_list = [1,2,70,4,10,29]

    result = bubble_sort(nums_list)

    print(result)