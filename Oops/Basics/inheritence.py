class Polygon:
    def __init__(self,sides):
        self.sides = sides
        
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):     # This is called method overriding
        print("A Triangle is a polygon with three sides")
        Polygon.display_info(self)  # inheritence we are using super class actions and methods



if __name__ == '__main__':
    
    triangle1 = Triangle([2,10,5])
    result =triangle1.get_perimeter()
    print(result)
    triangle1.display_info()