from mimetypes import init
import os
import sys
import random

# Global parameters of the generated baord
columns, rows = (5, 6)

# initilazes an empty Matrix/board with the 2 given parameter
def initEmptyMatrix(width, height):
    # width=coluumns height=rows
    matrix = [[0 for x in range(width)] for y in range(height)]


# Generates a borad with no empty field.
# you can set how diverse map you want.
def generateBoardFullRandom(columns, rows, numOfDifferentTiles):
    matrix = [[0 for x in range(columns)] for y in range(rows)]
    # filling out the board
    for i in range(rows - 1, -1, -1):
        for j in range(0, columns):
            matrix[i][j] = random.randrange(1, numOfDifferentTiles)
    return matrix


def writeBoardToFile(matrix, columns, rows, fileName):
    f = open(os.path.join(sys.path[0], fileName), "w")
    # writing out the data of the board
    f.write(str(columns) + ";" + str(rows) + "\n")
    # writing out the board
    for i in range(rows - 1, -1, -1):
        for j in range(0, columns):
            f.write(str(matrix[i][j]))
            if j != columns - 1:
                f.write(";")
        if i != 0:
            f.write("\n")
    #
    f.close


def main():
    Matrix = initEmptyMatrix(columns, rows)
    Matrix = generateBoardFullRandom(columns, rows, numOfDifferentTiles=5)
    writeBoardToFile(Matrix, columns, rows, "Test01.csv")
    print(Matrix)


# main()
