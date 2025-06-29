#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # MOD = 10**9 + 7
    # div_row = [0 for _ in range(m+1)]
    # wall = div_row
    # div_row[0] = 1
    
    # for i in range(1, m+1):
    #     for b in range(1, 5):
    #         if i - b >= 0:
    #             div_row[i] = (div_row[i] + div_row[i - b]) % MOD
   return "still not understand" 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
    