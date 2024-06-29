from datetime import datetime
from block import Block
from blockchain import Blockchain


blockchain = Blockchain()

# Add a new block to the blockchain
id = 1
new_block2 = Block(
    id = id + 1,
    data = {'price':10,'name':'prd1'},
    timestamp = datetime.now(),
    prev = blockchain.chain[-1].hash
)
id = id + 1
new_block3 = Block(
    id = id + 1,
    data = "simple data",
    timestamp = datetime.now(),
    # prev = blockchain.chain[-1].hash
    prev = blockchain.chain[-1].hash
)

blockchain.add_block(new_block2)
blockchain.add_block(new_block3)

# Verify that the new blocks has been added
for block in blockchain.chain:
    print(
        f"Block : {block.id}\n",
        f"Data: {block.data}\n",
        f"Timestamp: {block.timestamp}\n",
        f"Prev Hash: {block.prev}\n",
        f"Hash: {block.hash}\n",
    )
    
