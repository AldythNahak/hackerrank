#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def sortedSum(a):
    MOD = 10**9 + 7
    total = 0
    prefix = []

    for val in a:
        prefix.append(val)
        prefix.sort()
        for i in range(len(prefix)):
            total = (total + prefix[i] * (i + 1)) % MOD

    return total


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a_count = int(input().strip())

    # a = []

    # for _ in range(a_count):
    #     a_item = int(input().strip())
    #     a.append(a_item)

    # result = sortedSum(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    
    print(sortedSum([9,5,8]))
