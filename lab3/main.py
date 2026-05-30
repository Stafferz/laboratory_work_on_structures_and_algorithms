class QueueTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def move_elements(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            self.move_elements()

        if not self.stack_out:
            raise IndexError("Очередь пуста")

        return self.stack_out.pop()

    def front(self):
        if not self.stack_out:
            self.move_elements()

        if not self.stack_out:
            raise IndexError("Очередь пуста")

        return self.stack_out[-1]

    def clear(self):
        self.stack_in.clear()
        self.stack_out.clear()
        
if __name__ == "__main__":
    q = QueueTwoStacks()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Первый элемент:", q.front())

    print("Удалён элемент:", q.dequeue())
    print("Удалён элемент:", q.dequeue())

    print("Первый элемент:", q.front())

    q.enqueue(40)

    print("Удалён элемент:", q.dequeue())
    print("Удалён элемент:", q.dequeue())

    q.enqueue(50)
    q.enqueue(60)

    print("Первый элемент перед очисткой:", q.front())

    q.clear()

    try:
        print(q.front())
    except IndexError:
        print("Очередь пуста после очистки")