class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def add_two_numbers(self,number):
        real = self.real + number.real
        img = self.img + number.img
        result = Complex(real,img) 
        return result
    

if __name__ == '__main__':
    
    n1 = Complex(4,5)
    n2 = Complex(3,6)
    
    result = n1.add_two_numbers(n2)
    print(result.img)
    print(result.real)