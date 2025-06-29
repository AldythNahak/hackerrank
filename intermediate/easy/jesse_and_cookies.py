#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    import heapq
    heapq.heapify(A)
    
    totalMix = 0
    while len(A) > 1:
        cookies1 = heapq.heappop(A)
        cookies2 = heapq.heappop(A)
        
        if cookies1 >= k:
            return totalMix
        
        newCookies =  cookies1 + (2 * cookies2)
        heapq.heappush(A, newCookies)
        totalMix += 1          
    
    return totalMix if A[0] >= k else -1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # A = list(map(int, input().rstrip().split()))

    # result = cookies(k, A)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    # print(cookies(9, [2,7,3,6,4,6]))
    print(cookies(7, [1,2,3,9,10,12]))