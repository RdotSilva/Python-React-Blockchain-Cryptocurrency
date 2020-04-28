class Block:
    """
    Block: a unit of sotrage
    Store transactions in a blockchain that supports a cryptocurrency
    """

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return f"Block - data: {self.data}"


def main():
    block = Block("foo")
    print(block)


if __name__ == "__main__":
    main()
