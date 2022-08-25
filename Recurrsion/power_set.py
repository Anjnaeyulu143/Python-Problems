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
        if (In == ''):
            power_sets_list.append(Op)
            print(Op)
            return
        Op2 = Op
        Op2 += In[0]
        
        In = In[1:]
        
        helper(Op,In)
        helper(Op2,In)
        
        
    helper('',string)


    return power_sets_list
    
    
if __name__ == "__main__":
    string = 'ab'
    result = genrate_subsets(string)
    
    print(result)