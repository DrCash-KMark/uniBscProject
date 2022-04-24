import os
import sys

#global values:
columns, rows = 5,5
#left down is zero zero in the matrix


#never call this function with number being 0 it leads to an infinte recursion
#indexing starts from 0
def tileChosed(x,y,matrix,number):
    numOfTilesHit=0
    if matrix[x][y]==number:
        matrix[x][y]=0
        numOfTilesHit+=1
        if y<rows-1:
            numOfTilesHit += tileChosed(x,y+1,matrix,number)
        if x<columns-1:
            numOfTilesHit +=tileChosed(x+1,y,matrix,number)
        if y>0:
            numOfTilesHit +=tileChosed(x,y-1,matrix,number)
        if x>0:
            numOfTilesHit +=tileChosed(x-1,y,matrix,number)
    return numOfTilesHit
        
def collapse(matrix):
    #collapse the colums downwards
    newPlaceId=-1
    for i in range(0,columns):
       for j in range(0,rows):
           if matrix[i][j]== 0 and newPlaceId==-1:
               newPlaceId=j
           if matrix[i][j]!=0 and newPlaceId!=-1:
               matrix[i][newPlaceId]=matrix[i][j] #collapsing the Tiles downwards
               newPlaceId+=1
               matrix[i][j]=0
       newPlaceId=-1
    
    #collapsing the colums leftwards
    newPlaceId=-1
    for i in range(0, columns):#columns-1):
        if matrix[i][0]==0 and newPlaceId==-1:
            newPlaceId=i
        if matrix[i][0]!=0 and newPlaceId!=-1:
            for j in range(0,rows):
                matrix[newPlaceId][j]=matrix[i][j]
                matrix[i][j]=0
            newPlaceId+=1

#this prints the matrix as a player wouuld see it
def printMatrixNice(matrix):
    print(str(columns) + ";" + str(rows))
    for i in range(rows-1,-1,-1):
        for j in range(0,columns):
            print(matrix[j][i], end=" ")
        print()
    print()

def initBoardFromFile(matrix,fileName):    
    f = open(os.path.join(sys.path[0], fileName), "r") 

    #f = open(pathToFile,'r')
    firstLine = f.readline().split(";")
    w = int(firstLine[0])
    h = int(firstLine[1])
    #this reads in the board from a file which looks as a player would see
    matrix = [[0 for x in range(w)] for y in range(h)]
    for i in range(rows-1,-1,-1):
        stringLine = f.readline().split(";")
        for j in range(0,columns):
            matrix[j][i] = int(stringLine[j])

def main():
    print("Hello World!")
    
    #init the table for the game
    
    Matrix = [ [0, 0, 1,  2,1], [2, 1, 3, 2,1], [2, 0, 4, 0,0], [0, 0, 0, 0,0], [2, 4, 4, 4,1] ]
    initBoardFromFile(Matrix, "Map5x5.txt")
    printMatrixNice(Matrix)
    #Matrix = [[0 for x in range(0,columns)] for y in range(0,rows)]
    collapse(Matrix)
    printMatrixNice(Matrix)
    tileHit=0
    tileHit=tileChosed(2,1,Matrix,Matrix[2][1])
    printMatrixNice(Matrix)
    print(tileHit)
    collapse(Matrix)
    printMatrixNice(Matrix)
    
    
main()
