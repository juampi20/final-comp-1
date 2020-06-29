from random import randint

class Bingo():
    def __init__(self):
        self.container = []
        self.balls_removed = []
        self.sizeBoard = 15

    def push(self, item):
        self.container.append(item)

    def extract(self):
        try:
            return self.balls_removed.append(self.container.pop(randint(self.sizeContainer())))
        except IndexError:
            print("La lista esta vacia")

    def lastBall(self):
        if self.balls_removed != []:
            return self.balls_removed[-1]
        else:
            return 0

    def sizeContainer(self):
        return len(self.container)

    def getContainer(self):
        return self.container
    
    def getBallsRemoved(self):
        return self.balls_removed

    def getMajorBall(self):
        return max(self.container)

    def setSizeBoard(self, item):
        self.sizeBoard = item

    def getSizeBoard(self):
        return self.sizeBoard


        