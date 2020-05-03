from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain_instance():
    blockchain = Blockchain()

    # Check hash
    assert blockchain.chain[0] == GENESIS_DATA["hash"]
