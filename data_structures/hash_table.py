class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = {}

    def set(self, key, value):
        self.data.update({self.__hash(key): value})

    def get(self, key):
        return self.data[self.__hash(key)]

    def __str__(self):
        return str(self.__dict__)

    def __hash(self, key):
        hash = 0

        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % self.size

        return hash


hash_table = HashTable(50)
hash_table.set("grapes", 1000)
print(hash_table.get("grapes"))
