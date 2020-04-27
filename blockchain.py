class Block:
    """
    Block: a unit of sotrage
    Store transactions in a blockchain that supports a cryptocurrency
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Block - data: {self.data}"


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return f"Blockchain: {self.chain}"
