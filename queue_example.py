class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            return False
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]