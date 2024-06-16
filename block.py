from hashlib import sha256
from datetime import datetime

class Block():
    def __init__(self, id, data, timestamp, prev):
        self.id = id
        self.data = data
        self.timestamp = timestamp
        self.prev = prev
        self.hash = self.generate_hash()

    def display(self):
        return str(self.id) + str(self.data) + str(self.timestamp) + str(self.prev )

    def generate_hash(self):
        data = str(self.id) + str(self.data) + str(self.timestamp) + str(self.prev )
        return sha256(data.encode("UTF-8")).hexdigest()


block = Block(1, 'data', datetime.now(), '0')
print(block.display())
print(block.hash)
