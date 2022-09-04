def solve(nums_arr,k):
    
    
    j = i = 0
    neg_nums = []
    n = len(nums_arr)
    
    nums = []
    

    while j < n-1:
        if (j-i+1) < k:
            if (nums_arr[j] < 0):
                neg_nums.append(nums_arr[j])
            
            j += 1
        
        if (j-i+1) == k:
            
            if len(neg_nums) == 0:
                nums.append(0)
                
            else:
                nums.append(neg_nums[0])
                if (nums_arr[i] == neg_nums[0]):
                    neg_nums.pop(0) 
                
            i += 1
            
    print(nums)
        

if __name__ == "__main__":
    
    nums_arr = [-1,-7,8,-15,30,16,20]
    k = 3
    
    solve(nums_arr,3)