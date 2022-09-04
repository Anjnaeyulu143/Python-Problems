
# def solve(n,k,nums_arr):
    
#     cur_sum = pointer1 = pointer2 = mx = 0
    
#     while pointer2 < n:
        
#         cur_sum += nums_arr[pointer2]
        
#         if cur_sum == k:
#             mx = max(mx,pointer2-pointer1+1)
#             pointer2 += 1
            
#         while cur_sum > k:
#             cur_sum -= nums_arr[pointer1]
#             if cur_sum == k:
#                 mx = max(mx,pointer2-pointer1+1)
#             pointer1 += 1
            
#         pointer2 += 1
        
#     print(mx)

# if __name__ == '__main__':
    
#     n = 6
#     k = 5
    
#     nums_arr = [4,1,1,1,3,5]
    
#     solve(n,k,nums_arr)
    