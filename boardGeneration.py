from mimetypes import init
import os
import sys
import random

# Global parameters of the generated baord
columns, rows = (15, 16)
matrix = []

# initilazes an empty Matrix/board with the 2 given parameter
def initMapGenerator(width, height):
    # width=coluumns height=rows
    global columns, rows, matrix
    columns = width
    rows = height
    matrix = [[0 for x in range(width)] for y in range(height)]


# Generates a borad with no empty field.
# you can set how diverse map you want.
def generateBoardFullRandom(columns, rows, numberOfDifferentTile):
    matrix = [[0 for x in range(columns)] for y in range(rows)]
    # filling out the board
    for i in range(rows - 1, -1, -1):
        for j in range(0, columns):
            matrix[i][j] = random.randrange(1, numberOfDifferentTile)
    return matrix


def generateMultipleBoards(numberOfBoards, numberOfDifferentTile):
    for i in range(numberOfBoards):
        newBoard = generateBoardFullRandom(columns, rows, numberOfDifferentTile)
        # dont use : in file name
        name = (
            "GeneratedMaps\GeneratedMap"
            + str(i)
            + "Size"
            + str(columns)
            + "x"
            + str(rows)
            + ".csv"
        )
        writeBoardToFile(newBoard, columns, rows, name)


def writeBoardToFile(matrix, columns, rows, fileName):
    with open(os.path.join(sys.path[0], fileName), "w") as f:
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
        # f.close


def main():
    initMapGenerator(columns, rows)
    generateMultipleBoards(5, 4)
    newBoard = generateBoardFullRandom(columns, rows, 5)
    writeBoardToFile(newBoard, columns, rows, "fck.csv")
    writeBoardToFile(newBoard, columns, rows, "fck2.csv")


main()
