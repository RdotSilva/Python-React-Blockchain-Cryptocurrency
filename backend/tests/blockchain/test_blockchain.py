import pytest

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


# @pytest.fixture
# def blockchain_three_blocks():
#     blockchain = Blockchain()
#     for i in range(3):
#         blockchain.add_block(i)
#     return blockchain


def test_is_valid_chain():
    blockchain = Blockchain()

    for i in range(3):
        blockchain.add_block(i)

    Blockchain.is_valid_chain(blockchain.chain)


def test_is_valid_chain_bad_genesis():
    blockchain = Blockchain()

    for i in range(3):
        blockchain.add_block(i)

    blockchain.chain[0].hash = "evil_hash"

    with pytest.raises(Exception, match="genesis block must be valid"):
        Blockchain.is_valid_chain(blockchain)


# TODO last test is not passing. Double check test to make sure correct, if not go and fix code. Also look at pytest.fixture and try to get three blocks to work

