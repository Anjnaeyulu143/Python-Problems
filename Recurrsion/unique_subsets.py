



    

def solve(string):
    unique_subsets_list = []
    
    def unique_subsets(OP,IN):
    
        if (IN == ""):
            if OP not in unique_subsets_list:
                unique_subsets_list.append(OP)
            return


        OP2 = OP
        OP2 += IN[0]
        
        IN  = IN[1:]
        
        unique_subsets(OP,IN)
        unique_subsets(OP2,IN)
    
    unique_subsets('',string)
    
    print(unique_subsets_list)


if __name__ == '__main__':
    string = 'aab'
    solve(string)
    