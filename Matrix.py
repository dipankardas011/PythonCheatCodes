

def printMat(mat):
    """print matrix"""
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()

def printLeftDiag(mat):

    """printLeft Diagonal"""
    rowIdx, colIdx=0,0
    for i in mat:
        for j in i:
            if rowIdx == colIdx:
                print(j, end=' ')
            else:
                print('.', end=' ')
            colIdx+=1
        print()
        rowIdx+=1
        colIdx=0



if __name__ == '__main__':
    mat = [[1,1,0],[0,1,0],[1,1,1]]
    printMat(mat)
    print()
    printLeftDiag(mat)