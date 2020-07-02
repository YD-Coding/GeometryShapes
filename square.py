from math import sqrt
class Square:
    def __init__(self, rib):
        self.rib = rib
    
    def area(self):
        return self.rib ** 2
    
    def scope(self):
        return self.rib * 4
    
    def diagonals(self):
        return sqrt((self.rib ** 2) + (self.rib ** 2))