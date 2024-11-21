class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object() 

    def primary_hash(self, key):
        return hash(key) % self.size

    def secondary_hash(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        idx = self.primary_hash(key)
        step = self.secondary_hash(key)

        while self.table[idx] is not None and self.table[idx] is not self.deleted:
            idx = (idx + step) % self.size

        self.table[idx] = (key, value)

    def search(self, key):
        idx = self.primary_hash(key)
        step = self.secondary_hash(key)

        while self.table[idx] is not None:
            if self.table[idx] is not self.deleted and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + step) % self.size

        return None

    def delete(self, key):
        idx = self.primary_hash(key)
        step = self.secondary_hash(key)

        while self.table[idx] is not None:
            if self.table[idx] is not self.deleted and self.table[idx][0] == key:
                self.table[idx] = self.deleted
                return True
            idx = (idx + step) % self.size

        return False

# Prueba de la tabla hash
hash_table = HashTableDoubleHashing(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

print(hash_table.search("key1"))  # value1
print(hash_table.search("key2"))  # value2
print(hash_table.search("randomkey")) # None
hash_table.delete("key1")
print(hash_table.search("key1"))  # None
