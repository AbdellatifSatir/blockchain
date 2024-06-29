from block import Block
from datetime import datetime

class Blockchain():

    def __init__(self):
        self.chain = [self.new_genesis_block()]
        self.difficulty = 2 #zeros

    def __len__(self):
        return len(self.chain)

    # First block (genesis) prev = 0
    def new_genesis_block(self):
        return Block(id=1, data=None, timestamp=datetime.now(), prev=0)
    
    def add_block(self, new_block):
        # new_block.id = int(self.chain[-1].id) + 1
        new_block.prev = self.chain[-1].hash
        # new_block.hash = new_block.generate_hash()
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def verify_block(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]
            if((current_block.prev != prev_block.hash) or (current_block.hash != current_block.generate_hash())):
                return False
        return True
    
    


