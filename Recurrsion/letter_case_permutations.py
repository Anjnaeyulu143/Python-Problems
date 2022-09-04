
def solve(string):
    
    letter_case_list = []
    
    def letter_case(OP,IN):
        
        if (len(IN) == 0):
            letter_case_list.append(OP)
            return
        
        
        if IN[0].isalpha() == True:
            OP1 = OP
            OP2 = OP
            
            OP1 += IN[0].lower()
            OP2 += IN[0].upper()
            
            IN = IN[1:]
            
            letter_case(OP1,IN)
            letter_case(OP2,IN)
            
        else:
            OP1 = OP 
            
            OP1 += IN[0]
            IN = IN[1:]
            
            letter_case(OP1,IN)
            
        
        
    letter_case("",string) 
    
    print(letter_case_list)
1


if __name__ == '__main__':
    string = 'a2B1'
    
    solve(string)