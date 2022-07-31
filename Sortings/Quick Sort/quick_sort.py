# Quick Sort T.C O(nlog n) in average and best cases, O(n2) in worst cases


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
    
    test_cases = [
        [25,10,1,5,20,3],
        [8,0,1,20,3,1,49],
        [29,1,1000,2,4,100]
        ]
    
    for nums_list in test_cases:
        quick_sort(nums_list,0,len(nums_list)-1)
        print(nums_list)
    
    