from hashlib import sha256

class Block():

    def __init__(self, id, data, timestamp, prev):
        self.id = str(id)
        self.data = str(data)
        self.timestamp = str(timestamp)
        self.prev = str(prev)
        self.hash = self.generate_hash()

    def display(self):
        return self.id + self.data + self.timestamp + self.prev

    def generate_hash(self):
        data = self.id + self.data + self.timestamp + self.prev
        return sha256(data.encode("UTF-8")).hexdigest()
