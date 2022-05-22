from random import choice

# this is imported for testing
import boardGeneration

# this file contain the logic behind the pure random selector
Rows, Columns = (0, 0)
Matrix = [[0 for x in range(Columns)] for y in range(Rows)]
possibleOptions = []

# TODO fix because this doesn't initialize the file as a class
def initRandomPlayer(matrix, columns, rows):
    global Rows, Columns, Matrix
    Rows = rows
    Columns = columns
    Matrix = matrix


# with at least 2 connected
def findPossibleOptions():
    global possibleOptions, Rows, Columns, Matrix
    for i in range(0, rows):
        for j in range(0, columns):
            if Matrix[i][j] != 0:

                if i == rows:
                    if matrix[i][j] == matrix[i][j + 1]:
                        possibleOptions.append(str(i) + ";" + str(j))
                else:
                    if (
                        matrix[i][j] == matrix[i][j + 1]
                        or matrix[i][j] == matrix[i + 1][j]
                    ):
                        possibleOptions.append(str(i) + ";" + str(j))


# finds all the tile coordinates which ar not empty
def findAllNonEmpty():
    for i in range(Rows - 1, -1, -1):
        for j in range(0, Columns):
            if Matrix[i][j] != 0:
                possibleOptions.append(str(i) + ";" + str(j))


# return the cordinates of a selected tile
# format rowsIndex ; columIndex #TODO look into this statment
def selecTile():
    global possibleOptions
    chosen = choice(possibleOptions)
    return chosen


def main():
    Matrix = boardGeneration.generateBoardFullRandom(
        columns=5, rows=6, numOfDifferentTiles=5
    )
    initRandomPlayer(Matrix, columns=15, rows=16)
    findPossibleOptions()
    Coordinates = selecTile().split(";")
    print("row: " + Coordinates[0] + " Colum: " + Coordinates[1])


main()
