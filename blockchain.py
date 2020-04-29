from block import Block, genesis, mine_block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = [genesis()]

    def add_block(self, data):
        # Use the last block to determine where to add the next block
        last_block = self.chain[-1]
        self.chain.append(mine_block(last_block, data))

    def __repr__(self):
        return f"Blockchain: {self.chain}"


def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)


if __name__ == "__main__":
    main()
