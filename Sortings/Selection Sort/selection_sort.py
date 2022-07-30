# Selection Sort T.C in O(n2)


def sorted_list(nums_arr):
    
    n = len(nums_arr)
    
    for i in range(n-1):
        for j in range (i+1,n):
            if (nums_arr[i] > nums_arr[j]):
                nums_arr[i],nums_arr[j] = nums_arr[j],nums_list[i]
                
    return nums_arr

if __name__ == '__main__':

    nums_list = [18,39,2,10,5]

    result = sorted_list(nums_list)

    print(result)