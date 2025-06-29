import sys

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, elem):
        self.items.append(elem)
        
    def dequeue(self):
        if self.items:
            self.items.pop(0)
            
    def getHead(self):
        if self.items:
            return self.items[0]
        return None
    
    def __str__(self):
        print(self.getHead())


if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    stack = Queue()
    
    for _ in range(tests):
        q = sys.stdin.readline().strip().split()
        
        match int(q[0]):
            case 1:
                stack.enqueue(int(q[1]))
            case 2:
                stack.dequeue()
            case 3:
                stack.__str__()
                # sys.stdout(stack.getHead())
            