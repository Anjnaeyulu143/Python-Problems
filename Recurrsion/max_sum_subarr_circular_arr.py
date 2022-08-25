def solve(nums_arr):
    
    cur_min_sum = 0 
    
    n = len(nums_arr)
    
    min_sum = nums_arr[0]
    
    pr_arr = [i for i in range(n)]
    
    pr_arr[0] = nums_arr[0]
    
    for i in range(len(nums_arr)):
        cur_min_sum = min(cur_min_sum + nums_arr[i],nums_arr[i])
        min_sum = min(cur_min_sum,min_sum)
        
    
    
    for i in range(1, (n)):
        pr_arr[i] = nums_arr[i] + pr_arr[i-1]
        
   
    max_subarr_sum = pr_arr[len(pr_arr) - 1] - min_sum


    print(max_subarr_sum)
    print(min_sum)
    print(pr_arr[len(pr_arr)-1])

if __name__ == '__main__':
    
    nums_arr = [10,1,2,-1,5,-2]
    
    result = solve(nums_arr)