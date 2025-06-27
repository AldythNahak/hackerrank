#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    n = len(customers)
    trade = {}
    mostActive = []
    
    for name in customers:
        if not trade.get(name):
            trade[name] = 0
            
        trade[name] += 1    
        tradePercentage = (trade[name] / n) * 100

        if tradePercentage >= 5 and name not in mostActive:
            mostActive.append(name)
            
    return sorted(mostActive)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # customers_count = int(input().strip())
    
    # customers = []

    # for _ in range(customers_count):
    #     customers_item = input()
    #     customers.append(customers_item)

    # result = mostActive(customers)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
    
    result = mostActive(["Alpha",
"Beta",
"Zeta",
"Beta",
"Zeta",
"Zeta",
"Epsilon",
"Beta",
"Zeta",
"Beta",
"Zeta",
"Beta",
"Delta",
"Zeta",
"Beta",
"Zeta",
"Beta",
"Zeta",
"Beta",
"Zeta",
"Beta"])
    print(result)
