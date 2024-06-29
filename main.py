from datetime import datetime
from block import Block
from blockchain import Blockchain


blockchain = Blockchain()

# Add a new block to the blockchain without mine
# id = 1
# new_block2 = Block(
#     id = id + 1,
#     data = {'price':10,'name':'prd1'},
#     timestamp = datetime.now(),
#     prev = blockchain.chain[-1].hash
# )
# id = id + 1
# new_block3 = Block(
#     id = id + 1,
#     data = "simple data",
#     timestamp = datetime.now(),
#     prev = blockchain.chain[-1].hash
# )
# blockchain.add_block(new_block2)
# blockchain.add_block(new_block3)
print("Length of blockchain : ", blockchain.__len__())

# Mine
id = 1
new_block2 = Block(id=id+1,data={'price':10,'name':'prd1'},timestamp=datetime.now(),prev=blockchain.chain[-1].hash)
id = id + 1
new_block3 = Block(id=id+1,data="simple data",timestamp=datetime.now(),prev=blockchain.chain[-1].hash)

print("Mine block....")
blockchain.add_block(new_block2)
print("Mine block....")
blockchain.add_block(new_block3)

print("Length of blockchain : ", blockchain.__len__())


# Verify that the new blocks has been added
for block in blockchain.chain:
    print(
        f"Block : {block.id}\n",
        f"Data: {block.data}\n",
        f"Timestamp: {block.timestamp}\n",
        f"Prev Hash: {block.prev}\n",
        f"Hash: {block.hash}\n",
    )

# Verify the blocks
print("Verified Block : ",blockchain.verify_block())

# Change an existing block and verify
# print(blockchain.chain[-1].data)
# blockchain.chain[-1].data = "this data has been changed"
# print(blockchain.chain[-1].data)
# print("Verified Block : ",blockchain.verify_block())

