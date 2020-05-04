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


def test_mine_block_leading_zeros():
    # Set up a block
    last_block = Block.genesis()
    data = "test-data"
    block = Block.mine_block(last_block, data)

    # Check that the block hash has the correct number of leading zeros
    assert block.hash[0 : block.difficulty] == "0" * block.difficulty


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)

    # Loop through the const genesis, and compare genesis data with the const data
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value
