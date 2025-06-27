#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr = sorted(arr)
    mid = len(arr) // 2
    return arr[mid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # arr = [0,1,2,3,4,5,6]
    result = findMedian(arr)

    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
