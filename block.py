
class Block():
    def __init__(self, id, data, timestamp, prev):
        self.id = id
        self.data = data
        self.timestamp = timestamp
        self.prev = prev
        self.hash = self.generate_hash()

    def generate_hash(self):
        # return sha256(self.id + tojson(self.data) + self.prev + self.timestamp)
        pass


