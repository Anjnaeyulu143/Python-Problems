def filps(nums_arr,n,m):
    
    i = 0
    flip_count = 0
    
    while (i < len(nums_arr)):
        r = i
        while r <= (i+n+m) and r < len(nums_arr):
            if (r < i+m):
                if nums_arr[r] != 1:
                    flip_count += 1
            elif (r > i+m and r < i+n+m):
                if nums_arr[r] != 0:
                    flip_count += 1
            r += 1
        i += 1
    print(flip_count)

if __name__ == "__main__":
    n = 1
    m = 1
    ones_list = [0,0,1,1]
    
    filps(ones_list,n,m)
