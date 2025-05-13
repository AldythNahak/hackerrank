# # The lines `import math`, `import os`, `import random`, `import re`, and `import sys` are importing
# Python modules. These modules provide additional functionality that can be used in the script.
# Here is a brief explanation of each module:
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'minesweeper' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. STRING_ARRAY bom
#

def minesweeper(N, bom):
    maxBom = 50
    mapWidth = 10
    mapLength = 10
    mapLayout = []
    countPlaceBom = 0
    
    for i in range(mapLength) :
        mapLayout.append(["."] * mapWidth)
            
    for i, coordinate in enumerate(bom):
        if countPlaceBom > maxBom:
            break
        
        i, j = map(int, coordinate.split(','))
        mapLayout[i-1][j-1] = "x"
        countPlaceBom += 1 
       
    def fillWarn(i, j):
        bomb_count = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if 0 <= ni < mapLength and 0 <= nj < mapWidth:
                    if mapLayout[ni][nj] == 'x':
                        bomb_count += 1
        return bomb_count
    
    for i in range(mapLength):
        for j in range(mapWidth):
            if mapLayout[i][j] == '.':
                mapLayout[i][j] = str(fillWarn(i, j)) if fillWarn(i, j) > 0 else '.'
        
            
    # for i in range(mapLength) :
    # ......1x1.
    # 11..11211.
    # x2..1x1...
    # x3..111...
    # x421....11
    # 2xx1....1x
    # 2321....11
    # x1........
    # 11.1221...
    # ...1xx1...
    joinMap = ("".join(m) for m in mapLayout)    
    
    return joinMap

print(minesweeper(11, ["1,8","3,1","4,1","5,1","3,6","6,2","6,3","6,1","8,1","10,5","10,6"]))