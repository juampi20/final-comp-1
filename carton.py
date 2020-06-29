from bingo import Bingo
from random import randint

class Carton:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.numbers = [randint(1, 91) for num in range(1, self.size + 1)]
        
    def getNumbers(self):
        return self.numbers
    