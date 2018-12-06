class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)

q = Queue()

q.enqueue(50)
q.enqueue(60)
q.enqueue('Dog')
q.enqueue('Hello')
q.enqueue(52)
q.enqueue(62.5)
q.size()
q.isEmpty()
q.display()
q.dequeue()
q.display()