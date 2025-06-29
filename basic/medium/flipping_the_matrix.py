#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n = len(matrix) // 2
    total = 0
    
    for i in range(n):
        for j in range(n):
            t_left = matrix[i][j]
            t_right = matrix[i][2 * n - 1 - j]
            b_left = matrix[2 * n - 1 - i][j]
            b_right = matrix[2 * n - 1 - i][2 * n - 1 - j]
            total += max(t_left, t_right, b_left, b_right)
    
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

    # print(flippingMatrix([[1,2],[3,4]]))