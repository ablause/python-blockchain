from Block import Block


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(
            previous_hash='0000',
            proof=100
        )

    # builds new block and adds to the chain
    def new_block(self, proof, previous_hash=None):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash or self.last_block.hash,
            transactions=self.pending_transactions,
        )

        self.pending_transactions = []

        self.chain.append(block)

        return block

    def new_transaction(self, sender, receiver, amount):  # declares data of transactions
        self.pending_transactions.append({
            sender: sender,
            receiver: receiver,
            amount: amount
        })

        return self.last_block.index + 1

    @staticmethod
    # checks whether the blockchain is valid
    def confirm_validity(block, previous_block):
        if previous_block.index + 1 != block.index:
            return False
        elif previous_block.hash != block.previous_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False

        return True

    @property
    def last_block(self) -> Block:  # returns the last block in the chain
        return self.chain[-1]

# ================= #


blockchain = BlockChain()

print('Get ready mining about to start')

# proof = blockchain.proof_of_work()

t1 = blockchain.new_transaction('Alexandre Blause', 'Killian', '2 ETH')
t2 = blockchain.new_transaction('Alexandre Blause', 'Killian', '3 ETH')
t3 = blockchain.new_transaction('Alexandre Blause', 'Killian', '9 ETH')

block = blockchain.new_block('miner_4145', blockchain.last_block.index)

print('Mining has successful')

print(blockchain.chain)
