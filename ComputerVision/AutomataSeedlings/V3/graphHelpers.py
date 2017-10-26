import numpy as np
import matplotlib.pyplot as plt

# mapIdentityTopology( MIT )
# Given a binary matrix, number every 1 uniquely.
def MIT( matrix ):

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    matrixOut = np.zeros( matrix.shape, dtype=np.int)

    idCounter = 1

    for col in range(maxCols):
        for row in range(maxRows):
            if(matrix[row,col] > 0):
                matrixOut[row,col] = int(idCounter)
                idCounter += 1

    return (matrixOut,idCounter-1)


def adjacentNodes_D( matrix, location, edgeValRef ):

    element = matrix[location]

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]


    t = set()
    ## Find Adjacency ##

    # Left
    if (col-1) >= 0  and (row-1) >= 0 and matrix[row-1,col-1] > 0:
        # Left Top
        edgeValRef[element-1][int(matrix[row-1,col-1])-1] = 1
        t.add( str(int(matrix[row-1,col-1])) )
    if (col-1) >= 0 and matrix[row,col-1] > 0:
        # Left Middle
        edgeValRef[element - 1][int(matrix[row,col-1]) - 1] = 2
        t.add(str(int(matrix[row,col-1] )))
    if (col-1) >= 0 and (row+1) < maxRows and matrix[row+1,col-1] > 0:
        # Left Bottom
        edgeValRef[element - 1][int(matrix[row+1,col-1]) - 1] = 3
        t.add( str(int(matrix[row+1,col-1] ) ))

    # Middle
    if (row-1) >=0 and matrix[row-1,col] > 0:
        # Up
        edgeValRef[element - 1][int(matrix[row-1,col]) - 1] = 4
        t.add( str(int(matrix[row-1,col])) )
    if (row+1) < maxRows and matrix[row+1,col] > 0:
        # Down
        edgeValRef[element - 1][int(matrix[row+1,col]) - 1] = 5
        t.add( str(int(matrix[row+1,col] )) )

    # Right
    if  (col+1) < maxCols  and (row-1) >= 0 and matrix[row-1,col+1] > 0:
        # Right Top
        edgeValRef[element - 1][int(matrix[row-1,col+1]) - 1] = 6
        t.add( str( int(matrix[row-1,col+1]) ) )
    if  (col+1) < maxCols and matrix[row,col+1] > 0:
        # Right Middle
        edgeValRef[element - 1][int(matrix[row,col+1]) - 1] = 7
        t.add( str( int(matrix[row,col+1]) ))
    if (col+1) < maxCols and (row+1) < maxRows and matrix[row+1,col+1] > 0:
        # Right Bottom
        edgeValRef[element - 1][int(matrix[row+1,col+1]) - 1] = 8
        t.add( str( int(matrix[row+1,col+1]) ) )

    return t


def ACN_D( matrix , nNodes ):
    # Itterate through by column.

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    out = dict()

    edgeVals = np.zeros(shape=(nNodes,nNodes),dtype=np.int)

    for col in range( maxCols ):
        for row in range( maxRows ):

            element = matrix[row,col]

            # Make sure it's not a blank cell"and matrix[row,col] > 0"
            # Add adjacent nodes from top left to bottom right.
            if element > 0:
                ## Find Adjacency ##
                out[str(int(element))] = adjacentNodes_D(matrix, (row,col), edgeVals)

    return (out,edgeVals)

def annotateWeightedPathVect(path, idArray, nameArray):
    idDict = dict()
    newPath = []

    for elm in path:
        newPath.append(str(elm))

    iCount = 0
    for elm in idArray:
        idDict[elm] = nameArray[iCount]
        iCount+=1

    weightIndex = 1
    while( weightIndex+1 < len(path) ):
        newPath[weightIndex] = idDict[path[weightIndex]]
        weightIndex+=2

    return newPath

def assignPathWeights(path,edgeValMat):

    annotatedPath = []
    edgeBuffer = []

    for node in path:
        edgeBuffer.append( int(node) )

        if len(edgeBuffer) >= 2:
            #print( edgeValMat[edgeBuffer[0]-1][edgeBuffer[1]-1] )
            annotatedPath.append( edgeValMat[edgeBuffer[0]-1][edgeBuffer[1]-1] )
            edgeBuffer = [edgeBuffer[1]]

        annotatedPath.append(int(node))

    return annotatedPath


def compressList(lst, keepPos):

    newLst = []

    idx = keepPos - 1
    while (idx + (keepPos-1) < len(lst)):
        newLst.append( lst[idx] )
        idx += keepPos

    return newLst

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def longestSublists(lsts):
    longest = []
    subLists = []

    for lst in lsts:
        if (len(lst) > len(longest)):
            longest = lst

    for lst in lsts:
        if(len(lst) == len(longest) ):
            subLists.append(lst)

    return subLists

def lcs(S, T):
    m = len(S)
    n = len(T)
    counter = [[0] * (n + 1) for x in range(m + 1)]
    longest = 0
    lcs_set = []
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    lcs_set = []
                    longest = c
                    lcs_set.append(S[i - c + 1:i + 1])
                elif c == longest:
                    lcs_set.append(S[i - c + 1:i + 1])

    return lcs_set[0]

def simContinuity(l1, l2):

    return len(lcs(l1, l2)) / float(max(len(l1), len(l2)))



def pathSig(mat):
    LABELD_EDGE_WEIGHTS = ["LT", "LM", "LB", "MT", "MB", "RT", "RM", "RB"]
    EDGE_WEIGHTS = [1, 2, 3, 4, 5, 6, 7, 8]

    outMat, nNodes = MIT(mat)
    acn, edgeValMat = ACN_D(outMat, nNodes)

    paths = []
    visited = set()

    for outerNodeID in range(1,len(acn)+1):
        for nodeID in range(2, len(acn) + 1):
            if outerNodeID != nodeID and not( (outerNodeID,nodeID)  in visited ):
                tmp = list(dfs_paths(acn, str(outerNodeID), str(nodeID)))
                for path in tmp:
                    annotatedPath = assignPathWeights(path, edgeValMat)
                    paths.append( compressList(annotateWeightedPathVect(annotatedPath, EDGE_WEIGHTS, LABELD_EDGE_WEIGHTS), 2) )

                visited.add( (outerNodeID,nodeID) )
                visited.add( (nodeID, outerNodeID) )

    return paths

def getSubListsOfLenOrGreater(superList, length):
    nl = []

    for lst in superList:
        if len(lst) >= length:
            nl.append(lst)

    return nl

def identityContinuity(path):
    deriv = []
    identDict = dict()
    idCounter = 1

    for elm in path:
        if not (elm in identDict.keys()):
            identDict[elm] = idCounter
            idCounter += 1

        deriv.append(identDict[elm])

    return deriv

def listContinuity(path):
    deriv = []
    prev = path[0]
    prevSwitch = 0

    for elm in path:
        if elm == prev:
            deriv.append(prevSwitch)
        else:
            prevSwitch = int(not prevSwitch)
            deriv.append(prevSwitch)

        prev = elm

    return deriv


def adjacentNodes( matrix, location ):

    element = matrix[location]

    row = location[0]
    col = location[1]

    maxRows = matrix.shape[0]
    maxCols = matrix.shape[1]

    t = Node( element )
    ## Find Adjacency ##

    # Left

    if (col-1) >= 0  and (row-1) >= 0 and matrix[row-1,col-1] > 0:
        # Left Top
        t.addChild( matrix[row-1,col-1] )
    if (col-1) >= 0 and matrix[row,col-1] > 0:
        # Left Middle
        t.addChild( matrix[row,col-1] )
    if (col-1) >= 0 and (row+1) < maxRows and matrix[row+1,col-1] > 0:
        # Left Bottom
        t.addChild( matrix[row+1,col-1] )

    # Middle
    if (row-1) >=0 and matrix[row-1,col] > 0:
        # Up
        t.addChild( matrix[row-1,col] )
    if (row+1) < maxRows and matrix[row+1,col] > 0:
        # Down
        t.addChild( matrix[row+1,col] )

    # Right
    if  (col+1) < maxCols  and (row-1) >= 0 and matrix[row-1,col+1] > 0:
        # Right Top
        t.addChild( matrix[row-1,col+1] )
    if  (col+1) < maxCols and matrix[row,col+1] > 0:
        # Right Middle
        t.addChild( matrix[row,col+1] )
    if (col+1) < maxCols and (row+1) < maxRows and matrix[row+1,col+1] > 0:
        # Right Bottom
        t.addChild( matrix[row+1,col+1] )

    return t


def drawBinMatrix( mat ):
    imgplot = plt.imshow(mat, interpolation="nearest", cmap="hot")
    plt.axis("off")
    win = plt.show()
    raw_input()
    plt.close()

def saveBinMatrixIMG( mat , path, name ):
    imgplot = plt.imshow(mat, interpolation="nearest", cmap="hot")
    plt.axis("off")
    plt.savefig(path+name+'.png')




def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


def generateRandomBinaryMatrix( shape, bits ):
    nRow = shape[0]
    nCol = shape[1]

    outMat = np.zeros(shape)

    for i in range(bits):
        uniqueRandFound = False
        while not uniqueRandFound:
            rRow = np.random.randint(nRow)
            rCol = np.random.randint(nCol)
            if outMat[rRow,rCol] != 1:
                outMat[rRow,rCol] = 1
                uniqueRandFound = True


    return outMat



def generateRandomConnectedBinaryMatrix( shape, bits ):
    nRow = shape[0]
    nCol = shape[1]

    outMat = np.zeros(shape)

    # Start Cell
    rRow = np.random.randint(nRow)
    rCol = np.random.randint(nCol)

    outMat[rRow, rCol] = 1


    for i in range(bits-1):
        uniqueRandFound = False
        while not uniqueRandFound:
            rRow = np.random.randint(nRow)
            rCol = np.random.randint(nCol)

            AN = adjacentNodes(outMat, (rRow,rCol))

            if outMat[rRow,rCol] != 1 and len(AN.children) > 0:
                outMat[rRow,rCol] = 1
                uniqueRandFound = True

    return outMat