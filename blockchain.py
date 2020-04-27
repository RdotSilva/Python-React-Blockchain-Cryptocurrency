class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data set of transactions.
    """

    def __init__(self):
        self.chain = []
