from datetime import datetime
from block import Block


block = Block(1, 'some data', datetime.now(), '0')
print(block.display())
print(block.hash)

