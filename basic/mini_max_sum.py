#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mins = sum(sorted(arr)[:4])
    maxs = sum(sorted(arr, reverse=True)[:4])
    print(mins, maxs)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    # arr = [1,2,3,4,5]
    miniMaxSum(arr)
