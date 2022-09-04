
# def solve(n):
    
#     open = n
#     close = n
    
#     def generate_brackets(open,close,OP):
        
#         if (open == 0 and close == 0):
            
#             print(OP)
            
#             return 
        
#         elif (open != 0):
#             OP1 = OP 
            
#             OP1 += "("
            
#             generate_brackets(open-1,close,OP1)
            
#         elif (close > open):
            
#             OP2 = OP 
            
#             OP2 += ")"
            
#             generate_brackets(open,close-1,OP2)
            
#     generate_brackets(open,close," ")



# if __name__ == "__main__":
    
    
#     n = 4
    
#     solve(n)


def fun (open,close,I):
    if open == 0:
        for i in range(close):
            I += ")"
        print(I)
        return
        
    if open < close:
        fun(open-1,close,I+"(")
        fun(open,close-1,I+")")
        
    if open == close:
        fun(open-1,close,I+"(")
        
    if close <= open:
        return
    
fun(2,2,'')