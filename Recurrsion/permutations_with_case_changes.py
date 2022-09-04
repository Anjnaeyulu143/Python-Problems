def solve(string):
    print(string)
    
    def case_change(OP,IN):
        if (len(IN) == 0):
            print(OP)
            return
        
        OP1 = OP
        OP2  = OP
        
        OP1 += IN[0]
        OP1 += IN[0].upper()
        IN = IN[1:]
        
        case_change(OP2,IN)
        
        case_change(OP1,IN)
        
        
         

    case_change(" ",string)



if __name__ == '__main__':
    string = 'abc'
    solve(string)