import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, validator):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.validator}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = {}

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", "Genesis Validator")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data, validator):
        if validator not in self.validators:
            raise Exception("Validator not found in the list of validators")
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, time.time(), data, validator)
        self.chain.append(new_block)

    def register_validator(self, validator, stake):
        self.validators[validator] = stake

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True