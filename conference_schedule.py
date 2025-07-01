#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxPresentations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY scheduleStart
#  2. INTEGER_ARRAY scheduleEnd
#

def maxPresentations(scheduleStart, scheduleEnd):
    presentation = list(zip(scheduleStart, scheduleEnd))
    # print(presentation)
    presentation.sort(key=lambda x: x[1])
    # print(presentation)
    
    count = 0
    lastEndTime = -1
    
    for s, e in presentation:
        if s >= lastEndTime:
            count += 1
            lastEndTime = e
            
    return count

            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # scheduleStart_count = int(input().strip())

    # scheduleStart = []

    # for _ in range(scheduleStart_count):
    #     scheduleStart_item = int(input().strip())
    #     scheduleStart.append(scheduleStart_item)

    # scheduleEnd_count = int(input().strip())

    # scheduleEnd = []

    # for _ in range(scheduleEnd_count):
    #     scheduleEnd_item = int(input().strip())
    #     scheduleEnd.append(scheduleEnd_item)

    # result = maxPresentations(scheduleStart, scheduleEnd)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(maxPresentations([1,1,2,3], [2,3,3,4]))
