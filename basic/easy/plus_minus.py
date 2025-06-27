#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    positive, negative, zero = 0, 0, 0
    for num in arr:
        if num > 0: 
            positive += 1
            continue
        
        if num < 0: 
            negative += 1
            continue
        
        zero += 1
        
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # arr = [1,1,0,-1,-1]
    plusMinus(arr)
