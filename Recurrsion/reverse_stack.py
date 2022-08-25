


def insert(nums_arr, temp):
    
    if (len(nums_arr) == 0):
        
        return nums_arr.append(temp)
        
    
    popped_value = nums_arr.pop()
    
    insert(nums_arr,temp)
    
    nums_arr.append(popped_value)


def reverse(nums_arr):
    
    if (len(nums_arr) == 1):
        return nums_arr
    
    temp = nums_arr.pop()
    
    reverse(nums_arr)
    
    insert(nums_arr,temp)



if __name__ == '__main__':
    nums_arr = [[1,2,4,5,6],[100,2,39,10,67,99],[1,4,29,49,29],[0,1,2,3,4]]
    
    for nums in nums_arr:
        reverse(nums)
    
        print(nums)
    
    