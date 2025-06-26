#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    nRow = len(arr)
    d1 = 0 
    d2 = 0
    
    for i in range(nRow):
        d1 += arr[i][i]
        d2 += arr[i][nRow-i-1]

    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # arr = [[1,2,3],[4,5,6],[9,8,9]]
    result = diagonalDifference(arr)
    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
