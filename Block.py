import hashlib
import json
import time


class Block(object):
    # initial structure of the block class
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions

    @property
    def hash(self):  # producing the cryptographic hash of each block
        string_block = json.dumps(self.__dict__, sort_keys=True)
        block_string = string_block.encode()

        raw_hash = hashlib.sha256(block_string)

        hex_hash = raw_hash.hexdigest()

        return hex_hash
