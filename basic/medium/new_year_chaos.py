#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    bribe = 0
    for i in range(len(q)):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return
        
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribe += 1
            
    print(bribe)

if __name__ == '__main__':
    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
    
    minimumBribes([2,1,5,3,4])
    minimumBribes([2,5,1,3,4])
    minimumBribes([1,2,5,3,4,7,8,6])
    minimumBribes([5,1,2,3,7,8,6,4])
    minimumBribes([1,2,5,3,7,8,6,4])
