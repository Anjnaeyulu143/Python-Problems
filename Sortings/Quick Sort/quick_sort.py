def partition(nums_arr,l,h):
    
    pivot_element = nums_arr[l]
    
    s = l
    e = h
    
    while (s <= e):
    
        while (s < len(nums_arr) and nums_arr[s] <= pivot_element):
            s += 1
    
    
        while (nums_arr[e] > pivot_element):
            e -= 1
        
        if (s <= e):
            nums_arr[s], nums_arr[e] = nums_arr[e],nums_arr[s]
    
    nums_arr[l],nums_arr[e] = nums_arr[e],nums_arr[l]

    return e

def quick_sort(nums_arr,low,high):
    
    if (low < high):
        pivot = partition(nums_arr,low,high)
        
        quick_sort(nums_arr,low,pivot-1)
        quick_sort(nums_arr,pivot+1,high)
    
if __name__ == '__main__':
    
    nums_list = [21,10,1,0]
    quick_sort(nums_list,0,len(nums_list)-1)
    print(nums_list)