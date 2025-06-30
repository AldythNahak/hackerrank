#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countMax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY upRight as parameter.
#

def countMax(upRight):
    x = float('inf')
    y = float('inf')
    
    for c in upRight:
        x_c, y_c = c.strip().split()
        x_c, y_c = int(x_c), int(y_c)
        x = min(x, x_c)
        y = min(y, y_c)
        
    if x != float('inf'):
        return x * y
        
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    upRight_count = int(input().strip())

    upRight = []

    for _ in range(upRight_count):
        upRight_item = input()
        upRight.append(upRight_item)

    result = countMax(upRight)

    fptr.write(str(result) + '\n')

    fptr.close()
