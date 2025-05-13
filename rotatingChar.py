import os

def rotatingCharacter(text):
    results = []
    lines = text.splitlines()
    N, M = map(int, lines[0].split())
    # print(N)
    # print(M)
    matrix = lines[1:N+1]
    # print(matrix)
    
    Q = int(lines[N+1])
    
    for i in range(N+2, N+2+Q):
        R, target = lines[i].split()
        R = int(R) - 1  
        totOption = 0
        
        for col in range(M):
            tChar = target[col]
            isMatch = False
            rotationCount = float('inf')
            
            for row in range(N):
                if matrix[row][col] != tChar:
                    continue
                    
                lenBetweenChar = min((row - R) % N, (R - row) % N)
                rotationCount = min(rotationCount, lenBetweenChar)
                isMatch = True
            
            if not isMatch:
                totOption = -1  
                break
            
            totOption += rotationCount
        
        results.append(str(totOption))
    
    return "\n".join(results)


# text = """5 7
# sayqsps
# ytayayg
# suisvng
# armnubz
# rbcdefc
# 4
# 3 samsung
# 5 srinabc
# 5 abcdefg
# 1 zzzzzzz"""

# print(rotatingCharacter(text))

if __name__ == '__main__':
    text = ''
    try:
        while True:
            line = input()
            if line.strip() == '':
                break
            text += line + '\n'
    except EOFError:
        pass

    result = rotatingCharacter(text)

    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(result)