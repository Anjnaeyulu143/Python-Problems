# def helper(i, sub_set, nums, ans):
    
#     if i == len(nums):
#         ans.append(sub_set.copy())
#         return
    
    
#     sub_set.append(nums[i])
    
    
#     helper(i+1, sub_set, nums, ans)
    
    
#     sub_set.pop()
    
    
#     helper(i+1, sub_set, nums, ans)
    
    
#     return
def genrate_subsets(string):
    
    # print(string)
    
    power_sets_list = []
    
    def helper(Op,In):

        if (len(In) == 0):
            if Op not in power_sets_list:
                power_sets_list.append(list(map(int,Op)))
            return
        Op2 = Op
        Op2 += In[0]
        
        In = In[1:]
        
        helper(Op,In)
        helper(Op2,In)
        
        
    helper(string[0],string[1:])


    return power_sets_list
    
    
if __name__ == "__main__":
    string = [i for i in input().split()]
    result = genrate_subsets(string)
    
    for nums_list in result:
        print(sum(nums_list))
    