from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        # Use the last block to determine where to add the next block
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))

    def __repr__(self):
        return f"Blockchain: {self.chain}"

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the blockchain:
        1. The chain must start with the genesis block.
        2. Blocks must be formatted correctly
        """
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)


def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)


if __name__ == "__main__":
    main()
