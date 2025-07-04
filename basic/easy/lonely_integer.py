#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    for _, n in enumerate(a):
        if a.count(n) == 1:
            return n
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    # a = [1,2,3,4,3,2,1]
    result = lonelyinteger(a)
    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
