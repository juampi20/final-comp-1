from utilities import clear
from bingo import Bingo
from stack import Stack
from carton import Carton
from random import randint

def main():
    bingo = Bingo()
    stack = Stack()
    for num in range(1,91):
        bingo.push(num)
    
    clear()
    print(bingo.getContainer(), "\n")

    for i in range(5):
        stack.pushBoard(Carton(i, bingo.getSizeBoard()))

    print("Cartones:\n")
    for obj in stack.getBoards():
        print(obj.getNumbers(),"\n")
    

    input("\nPresione cualquier tecla para continuar...")

if __name__ == "__main__":
    main()    
