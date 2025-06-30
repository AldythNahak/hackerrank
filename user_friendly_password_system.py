#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

M = 10**9 + 7
P = 131

def hashPassword(s):
    hash_password = 0
    pw = 1
    for c in s:
        hash_password = (hash_password * P + ord(c)) % M
    return hash_password

def authEvents(events):
    current_password = ""
    log = []

    for action, password in events:
        if action == "setPassword":
            current_password = password

        elif action == "authorize":
            target_hash = int(password)
            current_hash = hashPassword(current_password)

            # Exact match
            if target_hash == current_hash:
                log.append(1)
                continue

            # Try adding 1 character at the end
            match = False
            pw = pow(P, len(current_password), M)  # P^len(current_password) % M

            for ascii_code in range(32, 127):  # Printable ASCII
                new_hash = (current_hash * P + ord(chr(ascii_code))) % M
                if new_hash == target_hash:
                    match = True
                    break

            log.append(1 if match else 0)

    return log


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # events_rows = int(input().strip())
    # events_columns = int(input().strip())

    # events = []

    # for _ in range(events_rows):
    #     events.append(input().rstrip().split())

    # result = authEvents(events)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    # print("Hash:", hashPassword("000A"))
    # print("Hash:", hashPassword("000AB"))
    print(authEvents([
        ["setPassword", "000A"], 
        ["authorize", "108738450"],
        ["authorize", "108738449"], 
        ["authorize", "244736787"]]))