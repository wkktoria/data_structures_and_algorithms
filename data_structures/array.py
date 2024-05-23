class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]

        del self.data[self.length - 1]
        self.length -= 1

        return last_item

    def delete(self, index):
        item = self.data[index]

        self.shift_items(index)

        return item

    def shift_items(self, index):
        for i in range(0, len(self.data) - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1


array = Array()

array.push('hi')
array.push('you')
array.push('!')

print(array.pop())

array.delete(1)

print(array)