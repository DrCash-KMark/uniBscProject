import os
import sys

# global values:
columns, rows = (15, 16)
# left down is zero zero in the matrix


# never call this function with number being 0 it leads to an infinte recursion
# indexing starts from 0
def tileChosed(x, y, matrix, number):
    numOfTilesHit = 0
    if matrix[x][y] == number:
        matrix[x][y] = 0
        numOfTilesHit += 1
        if y < rows - 1:
            numOfTilesHit += tileChosed(x, y + 1, matrix, number)
        if x < columns - 1:
            numOfTilesHit += tileChosed(x + 1, y, matrix, number)
        if y > 0:
            numOfTilesHit += tileChosed(x, y - 1, matrix, number)
        if x > 0:
            numOfTilesHit += tileChosed(x - 1, y, matrix, number)
    return numOfTilesHit


def collapse(matrix):
    # collapse the colums downwards
    newPlaceId = -1
    for w in range(0, columns):
        for h in range(0, rows):
            if (
                matrix[h][w] == 0 and newPlaceId == -1
            ):  # initalizing where to collapse the colum downwards
                newPlaceId = h
            if matrix[h][w] != 0 and newPlaceId != -1:
                matrix[newPlaceId][w] = matrix[h][w]  # collapsing the Tiles downwards
                newPlaceId += 1
                matrix[h][w] = 0
        newPlaceId = -1

    # collapsing the colums leftwards
    newPlaceId = -1
    for w in range(0, columns):  # columns-1):
        if matrix[0][w] == 0 and newPlaceId == -1:
            newPlaceId = w
        if matrix[0][w] != 0 and newPlaceId != -1:
            for h in range(0, rows):
                matrix[h][newPlaceId] = matrix[h][w]
                matrix[h][w] = 0
            newPlaceId += 1


# this prints the matrix as a player wouuld see it
def printMatrixNice(matrix):
    print(str(columns) + ";" + str(rows))
    for i in range(rows - 1, -1, -1):
        for j in range(0, columns):
            print(matrix[i][j], end=" ")
        print()
    print()


def initBoardFromFile(fileName):
    f = open(os.path.join(sys.path[0], fileName), "r")

    # f = open(pathToFile,'r')
    firstLine = f.readline().split(";")
    width = int(firstLine[0])
    height = int(firstLine[1])
    # this reads in the board from a file which looks as a player would see
    matrix = [[0 for x in range(width)] for y in range(height)]
    for i in range(height - 1, -1, -1):
        stringLine = f.readline().split(";")
        for j in range(0, width, 1):
            matrix[i][j] = int(stringLine[j])
    return matrix


# Return the score achived with the removal of numberOfTitlesHit
def calculateScore(numberOfTilesHit):
    return (numberOfTilesHit - 1) ^ 2


# The main loop of the game
def gameLoop(matrix):
    gameIsOn = True
    totalScore = 0
    printMatrixNice(matrix)
    while gameIsOn:
        # give the coordinates in a format of x;y for example: 1;2
        inputData = input()
        splitedData = inputData.split(";")
        xCoordinate = splitedData[0]
        yCoordinate = splitedData[1]
        #
        selectedTile = matrix[xCoordinate][yCoordinate]
        # testing if the selected tile can be chosen
        if selectedTile != 0:
            titleHit = tileChosed(xCoordinate, yCoordinate, matrix, selectedTile)
            collapse(matrix)
            score = calculateScore(titleHit)
            print(score)
            totalScore += score
        # since the collapse always moves item towards 0,0 if it is empty it means the game has ended because no mroe tiles remain.
        if matrix[0][0] == 0:
            gameIsOn = False


def main():
    print("Hello World!")

    # init the table for the game

    Matrix = [[0 for i in range(columns)] for j in range(rows)]
    Matrix = initBoardFromFile("Map5x6.txt")
    printMatrixNice(Matrix)
    # Matrix = [[0 for x in range(0,columns)] for y in range(0,rows)]
    collapse(Matrix)
    printMatrixNice(Matrix)
    tileHit = 0
    tileHit = tileChosed(2, 1, Matrix, Matrix[2][1])
    printMatrixNice(Matrix)
    print(tileHit)
    collapse(Matrix)
    printMatrixNice(Matrix)


main()
