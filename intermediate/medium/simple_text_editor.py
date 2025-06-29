import sys

class SimpleTextEditor:
    def __init__(self):
        self.text = ""
        self.listChange = []
        
    def append(self, word):
        self.listChange.append(self.text)
        self.text += word
        
        
    def delete(self, total_char):
        if len(self.text) >= total_char:
            self.listChange.append(self.text)
            self.text = self.text[:-total_char]
            
    def print(self, position):
        print(self.text[position-1])
        
    def undo(self):
        if self.listStateChange:
            self.text = self.listChange[-1]
            self.listChange.pop()
            
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    textEditor = SimpleTextEditor()
    
    for _ in range(n):
        inp = sys.stdin.readline().strip().split()
        
        match int(inp[0]):
            case 1:
                textEditor.append(inp[1])
            case 2:
                textEditor.delete(int(inp[1]))
            case 3:
                textEditor.print(int(inp[1]))
            case 4:
                textEditor.undo()