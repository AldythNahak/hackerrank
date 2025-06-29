#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    if len(s)%2 != 0 or len(s) > 10**3:
        return "NO"
    
    mapBracket = {"(": ")","[": "]", "{": "}"}
    openBracket = []
    
    for i, bracket in enumerate(s):
        if i == 0 and bracket in mapBracket.values():
            return "NO"
        
        if bracket not in mapBracket.keys() and bracket not in mapBracket.values():
            return "NO"
        
        if len(openBracket) == 0 and bracket in mapParentheses.values():
            return "NO"
        
        if mapBracket.__contains__(bracket):
            openBracket.append(bracket)
            continue
        
        lastOpenBracket = openBracket[-1]
        if mapBracket.get(lastOpenBracket) == bracket:
            openBracket.pop()
            continue
        else:
            return "NO"
            
    return "YES" if len(openBracket) == 0 else "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t = int(input().strip())
    
    # for t_itr in range(t):
    #     s = input()

    #     result = isBalanced(s)

    #     fptr.write(result + '\n')

    # fptr.close()

    print(isBalanced("{[()]}"))