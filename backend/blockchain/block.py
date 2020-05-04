import time

from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    "timestamp": 1,
    "last_hash": "genesis_last_hash",
    "hash": "genesis_hash",
    "data": [],
    "difficulty": 3,
    "nonce": "genesis_nonce",
}


class Block:
    """
    Block: a unit of sotrage
    Store transactions in a blockchain that supports a cryptocurrency
    """

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            "Block("
            f"timestamp: {self.timestamp}, "
            f"last_hash: {self.last_hash}, "
            f"hash: {self.hash},"
            f"difficulty: {self.difficulty},"
            f"nonce: {self.nonce})"
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        # return Block(
        #     timestamp=GENESIS_DATA["timestamp"],
        #     last_hash=GENESIS_DATA["last_hash"],
        #     hash=GENESIS_DATA["hash"],
        #     data=GENESIS_DATA["data"],
        # )
        # Instead of using above syntax use ** to unpack the entire dictionary
        return Block(**GENESIS_DATA)


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "foo")
    print(block)


if __name__ == "__main__":
    main()
