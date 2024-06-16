from block import Block
from datetime import datetime

class Blockchain():
    def __init__(self):
        self.chain = [self.new_genesis_block()]

    # first block
    def new_genesis_block():
        return Block(id=1, data=None, timestamp=datetime.now(), prev="0" )
    
    def add_block(self, new_block):
        new_block.prev = self.chain[-1].hash
        new_block.hash = new_block.generate_hash()
