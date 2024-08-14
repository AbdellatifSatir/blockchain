from hashlib import sha256

class Block():

    def __init__(self, id, data, timestamp, prev):
        self.id = str(id)
        self.data = str(data)
        self.timestamp = str(timestamp)
        self.prev = str(prev)
        self.hash = self.generate_hash()
        # self.nonce = 0 #iterations

    def display(self):
        return self.id + self.data + self.timestamp + self.prev #+ str(self.nonce)

    def generate_hash(self):
        data = self.id + self.data + self.timestamp + self.prev #+ self.nonce
        return sha256(data.encode("UTF-8")).hexdigest()
    
    # def mine_block(self, difficulty):
    #     target = '0' * difficulty
    #     while self.hash[:difficulty] != target:
    #         self.nonce += 1
    #         print(self.nonce)
    #         self.hash = self.generate_hash()
    #         print(self.hash)
    #     print(f"Block mined: {self.hash}")
    
