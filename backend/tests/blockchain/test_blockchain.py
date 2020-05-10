from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain_instance():
    blockchain = Blockchain()

    # Check hash
    assert blockchain.chain[0].hash == GENESIS_DATA["hash"]


def test_add_block():
    blockchain = Blockchain()
    data = "test-data"
    blockchain.add_block(data)

    # Check last block data is equal to test data
    assert blockchain.chain[-1].data == data


@pytest.fixture
def blockchain_three_blocks():
    blockchain = Blockchain()
    # Add 3 blocks to the blockchain instance
    for i in range(3):
        blockchain.add_block(i)
    return blockchain


def test_is_valid_chain(blockchain_three_blocks):
    # Test will pass if no exceptions raised
    Blockchain.is_valid_chain(blockchain_three_blocks)
