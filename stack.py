class Stack():
    def __init__(self):
        self.boards = []

    def pushBoard(self, item):
        self.boards.append(item)

    def getBoards(self):
        return self.boards
