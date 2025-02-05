# Required imports at top
import datetime
import hashlib
import json
from blockchain import Block

class Node:
    def __init__(self):
        self.blockchain = []
        self.blockchain_history = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block with previous hash of 0
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.datetime.now()),
            'transactions': [],
            'previous_hash': '0',
            'nonce': 0
        }
        # Calculate hash for genesis block
        genesis_block['hash'] = self.calculate_hash(genesis_block)
        self.blockchain.append(genesis_block)
        self.blockchain_history.append(genesis_block.copy())

    def calculate_hash(self, block):
        # Convert block to string and return SHA-256 hash
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def print_blockchain_state(self):
        print("\nCurrent Blockchain State:")
        for block in self.blockchain:
            print(f"\nBlock #{block['index']}")
            print(f"Hash: {block['hash']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Number of Transactions: {len(block['transactions'])}")

    def get_blockchain_history(self):
        return self.blockchain_history
    
node = Node()
node.print_blockchain_state()