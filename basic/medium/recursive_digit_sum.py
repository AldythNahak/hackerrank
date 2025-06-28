#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    concat_n = sum([int(d) for d in n]) * k
    
    def sumDigit(num):
        if len(num) == 1:
            return int(num)
        return sumDigit(str(sum([int(d) for d in num])))

    return sumDigit(str(concat_n))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = first_multiple_input[0]

    # k = int(first_multiple_input[1])

    # result = superDigit(n, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    
    print(superDigit("98750", 4))
