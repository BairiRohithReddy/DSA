'''
In this program we shall define and create a data type of our own which is called fraction
'''
class Fraction:
    
    def __init__(self, n, d) -> None:
        self.numerator = n
        self.denominator = d
        
    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'
    
    def __add__(self, other):
        temp_num = (self.numerator * other.denominator) + (self.denominator* other.numerator)
        temp_den = self.denominator * other.denominator
        
        return f'{temp_num}/{temp_den}'
    
    def __sub__(self, other):
        temp_num = (self.numerator * other.denominator) - (self.denominator* other.numerator)
        temp_den = self.denominator * other.denominator
        
        return f'{temp_num}/{temp_den}'
    
    def __mul__(self, other):
        temp_num = (self.numerator * other.numerator)
        temp_den = self.denominator * other.denominator
        
        return f'{temp_num}/{temp_den}'
    
    def __truediv__(self, other):
        temp_num = (self.numerator * other.denominator)
        temp_den = self.denominator * other.numerator
        
        return f'{temp_num}/{temp_den}'