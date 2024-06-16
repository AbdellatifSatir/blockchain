from block import Block
from datetime import datetime

class Blockchain():

    def __init__(self):
        self.chain = [self.new_genesis_block()]

    # First block (genesis) prev = 0
    def new_genesis_block():
        return Block(id=1, data=None, timestamp=datetime.now(), prev="0" )
    
    def display(self):
        return self.chain
    
    # def add_block(self, new_block):
    #     new_block.prev = self.chain[-1].hash
    #     new_block.hash = new_block.generate_hash()

blockchain = Blockchain()
print(blockchain.chain)