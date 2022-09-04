

def solve(n):

    
    ones = zeros = 0    # number of ones and zeros initalising with 0
    
    OP = ""        # we intializing final output as '' string
    
    def n_binary(ones,zeros,n,OP):
        
        if n==0:            # Base Condition to terminate
            print(OP)
            return  
        
        
        OP1 = OP     # We are initializing OP1 with OP 
        
        OP1 += "1"   # We are adding string 1 to the OP1
        
        n_binary(ones+1,zeros,n-1,OP1) 
        
        if ones > zeros :
            
            OP2 = OP 
            
            OP2 += "0"
            
            n_binary(ones,zeros+1,n-1,OP2)
        
            

    n_binary(ones,zeros,n,OP)


if __name__ == '__main__':
    n = 3
    
    solve(n)