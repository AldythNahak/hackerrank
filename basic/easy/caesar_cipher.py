#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encodeText = ""
    sLower = ord("a")
    sUpper = ord("A")
    
    for c in s:
        if not c.isalpha():
            encodeText += c
            continue

        if c.isupper():
            encode = (ord(c) - sUpper + k) % 26 + sUpper        
        else:
            encode = (ord(c) - sLower + k) % 26 + sLower
        
        encodeText += chr(encode)
        
    return encodeText

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
    
    # print(caesarCipher("abcdefghijklmnopqrstuvwxyz", 3))