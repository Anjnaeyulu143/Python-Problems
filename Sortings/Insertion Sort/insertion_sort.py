# Insertion Sort T.C O(n) in best case && O(n2) in worst case

def insertion_sort(nums_arr):
    
    n = len(nums_arr)
    
    for i in range(1,n):
        
        temp = nums_arr[i]
        a = -1

        
        for j in range(i-1,-1,-1):
            if (nums_arr[j] > temp):
                val = nums_arr[j]
                nums_arr[j+1] = val
            elif (nums_arr[j] < temp):
                a = j 
                break
        nums_arr[a+1] = temp
    return nums_arr

if __name__ == '__main__':

    nums_list = [2,20,10,100,1,2,3,4,5,6]

    result = insertion_sort(nums_list)
    print(result)
