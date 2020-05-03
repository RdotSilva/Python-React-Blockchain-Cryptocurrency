from backend.blockchain.block import Block, GENESIS_DATA


def test_mine_block():
    # Set up a block
    last_block = Block.genesis()
    data = "test-data"
    block = Block.mine_block(last_block, data)

    # Confirm block is instance of Block, has correct data, and last_lash
    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    # Check all fields in genesis against the const fields
    assert genesis.timestamp == GENESIS_DATA["timestamp"]
    assert genesis.last_hash == GENESIS_DATA["last_hash"]
    assert genesis.hash == GENESIS_DATA["hash"]
    assert genesis.data == GENESIS_DATA["data"]
