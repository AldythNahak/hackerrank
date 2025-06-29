#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    arr = sorted(arr)
    n = len(arr)
    pair = 0
    p1, p2 = 0, 1
    
    while p2 < n:
        total = arr[p2] - arr[p1]
        if total == k:
            pair += 1
            p1 += 1
            p2 += 1
        elif total < k:
            p2 += 1
        else:
            p1 += 1
            if p1 == p2:
                p2 += 1
            
    return pair

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    # result = pairs(k, arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    
    print(pairs(2, [1, 5, 3, 4, 2]))
