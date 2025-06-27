#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    dateParse = datetime.strptime(s, "%I:%M:%S%p")
    return dateParse.strftime("%H:%M:%S")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    # s = "12:01:00PM"

    result = timeConversion(s)

    # print(result)
    fptr.write(result + '\n')

    fptr.close()