class Block:
    """
    Block: a unit of sotrage
    Store transactions in a blockchain that supports a cryptocurrency
    """

    def __init__(self, data):
        self.data = data


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = []
