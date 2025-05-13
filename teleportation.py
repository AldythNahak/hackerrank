import math
import os
import random
import re
import sys

def teleportation(text):
    lines = text.strip().split('\n')
    # print(lines)
    numTest = int(lines[0])
    startLineTest = 1
    collectPLevel = []
    
    for _ in range(numTest):
        _, P1, P2 = map(int, lines[startLineTest].split())
        portal = list(map(int, lines[startLineTest + 1].split()))
        # print(portal)
        startLineTest += 2
        # print(startLineTest)
        # return
        
        pLevel = []
        for power in portal:
            diff1 = abs(power - P1)
            diff2 = abs(power - P2)
        
            if diff1 >= 11 and diff1 <= 14:
                diff1 = 2
            
            # print(f'{power} - {P1}')
            # print('-----')
            # print(f'{power} - {P2}')
            # print(f'{diff1} - {diff2}')
            # print(min(diff1, diff2))
            # if min(diff1, diff2) == 3:
            #     print(f'{power} - {P1}')
            #     print(f'{power} - {P2}')
            #     print(f'{diff1} - {diff2}')
            #     print('-----')]
            
            minVest = min(diff1, diff2)
            
            test = 0
            if minVest > 3:
                diff = minVest - 3
                test = minVest - diff
                print(power)
                
                
            # if test > 3:
            #     print(test)
            
            if minVest > 3:
                diff = minVest - 3
                minVest = minVest - diff
                
            pLevel.append(str(minVest))

        # print(pLevel)
        # print(pLevel2[1])

        collectPLevel.append(' '.join(pLevel))
    
    return '\n'.join(collectPLevel)
   
text = """2
5 2 11
8 4 14 1 13
12 5 15
16 18 4 9 5 10 6 13 1 0 19 1"""
print(teleportation(text))

# # 3 2 2 1 2
# # 1 2 1 3 0 3 1 2 3 3 2 3     
        
# if __name__ == '__main__':
#     text = ''
#     try:
#         while True:
#             line = input()
#             if line.strip() == '':
#                 break
#             text += line + '\n'
#     except EOFError:
#         pass

#     result = teleportation(text)

#     with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
#         fptr.write(result)