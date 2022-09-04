
def solve(string):
    
    OP = string[0]
    
    IN = string[1:]
    
    def permutations(OP,IN):
        
        if (len(IN) == 0):
            print(OP)
            return
        
        OP2 = OP
        OP2 += " "
        OP2 += IN[0]
        
        OP += IN[0]
        
        IN = IN[1:]
        
         
        permutations(OP2,IN)
        permutations(OP,IN)
        
    permutations(OP,IN)

if __name__ == "__main__":
    
    string = 'ABC'
    
    solve(string)
