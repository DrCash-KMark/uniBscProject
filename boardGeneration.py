import os
from random import random

def generateBoardFullRandom(matrix, columns, rows, numOfDifferentTiles):
    for i in range(rows-1,-1,-1):
        for j in range(0,columns):
            matrix[j][i]= random(1,numOfDifferentTiles)
