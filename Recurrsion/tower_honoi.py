
def solve(s,d,h,n):
    if (n == 1):
        print('moved {0} plate from {1} to {2}'.format(n,s,d))
        return

    solve(s,h,d,n-1)
    
    print('moved {0} plate from {1} to {2}'.format(n,s,d))
    
    solve(h,d,s,n-1)

if __name__ == "__main__":
    n = 3
    
    s = 'source'
    d = 'desination'
    h = 'helper'
    
    solve(s,d,h,n)