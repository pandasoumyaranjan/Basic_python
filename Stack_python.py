class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)

s = Stack()

print(s.isEmpty())
s.push(4)
s.push('Dog')
print(s.isEmpty())
print(s.size())
s.push(20)
s.push(35)
s.push('Hello')
s.push('Smruti')
s.push(8.4)
s.display()