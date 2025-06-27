#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    results = []
    for username in usernames:
        isFound = False
        for i in range(len(username)):
            for j in range(i+1, len(username)):
                if username[j] < username[i]:
                    isFound = True
                    break
            
            if isFound:
                break
        
        results.append("YES" if isFound else "NO")
    return results

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # usernames_count = int(input().strip())

    # usernames = []

    # for _ in range(usernames_count):
    #     usernames_item = input()
    #     usernames.append(usernames_item)

    # result = possibleChanges(usernames)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
    
    result = possibleChanges(["abc"])
    print("".join(result))
