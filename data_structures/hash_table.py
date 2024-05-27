class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def set(self, key, value):
        address = self.__hash(key)
        self.data[address] = (key, value)

    def get(self, key):
        address = self.__hash(key)
        return self.data[address]

    def keys(self):
        keys = []

        for i in range(0, len(self.data)):
            if self.data[i] is not None:
                keys.append(self.data[i][0])

        return keys

    def values(self):
        values = []

        for i in range(0, len(self.data)):
            if self.data[i] is not None:
                values.append(self.data[i][1])

        return values

    def __hash(self, key):
        hash = 0

        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % self.size

        return hash


hash_table = HashTable(50)
hash_table.set("grapes", 1000)
hash_table.set("apples", 54)
hash_table.set("oranges", 2)
print(hash_table.get("grapes"))
print(hash_table.keys())
print(hash_table.values())
