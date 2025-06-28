#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    n = len(petrolpumps)
    tank = 0
    petrolStart = 0
    petrolCount = 0
    
    for i in range(n):
        p1, p2 = petrolpumps[i]
        tank += p1 - p2
        petrolCount += tank
        
        if tank < 0:
            petrolStart = i + 1
            tank = 0
            
    if petrolCount < 0:
        return -1
    
    return petrolStart
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
