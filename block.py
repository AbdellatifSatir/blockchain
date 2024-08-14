from hashlib import sha256

class Block():

    def __init__(self, id, data, timestamp, prev):
        self.id = str(id)
        self.data = str(data)
        self.timestamp = str(timestamp)
        self.prev = str(prev)
        self.nonce = 0 #iterations
        self.hash = self.generate_hash()

    def display(self):
        return self.id + self.data + self.timestamp + self.prev + str(self.nonce)

    def generate_hash(self):
        data = self.id + self.data + self.timestamp + self.prev + str(self.nonce)
        return sha256(data.encode("UTF-8")).hexdigest()
    
    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            print("nonce=", self.nonce)
            self.hash = self.generate_hash()
            print(self.hash,'\n')
        print(f"Block mined: {self.hash}")
    
