def reverse_array(nums_arr,l,h):
    if (l<=h):
        nums_arr[l],nums_arr[h] = nums_arr[h],nums_arr[l]
        reverse_array(nums_arr,l+1,h-1)




if __name__ == '__main__':
    data_list = [[1,2,3,4,5],[10,9,8,7,6],[21,22,23,24,25,30],[8,2,1,3,5]]
    for nums_list in data_list:
        n = len(nums_list)-1
        reverse_array(nums_list,0,n)
        print(nums_list)