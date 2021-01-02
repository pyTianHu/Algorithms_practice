#FIFO - First In First Out
#LIFO - Last In First Out

class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return not self.items #Ez azért működik, mert egy üres lista automatikusan False-ra értékelődik pythonban
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self): 
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.isempty())
    s.push(3)
    print("3 pushed")
    print(s)
    print("5-7-8 pushed")
    s.push(5)
    s.push(7)
    s.push(8)
    print(s)
    print("pop function - pops the last value")
    print(s.pop())
    print(s.peek())
    print(s.size())
    
    
    