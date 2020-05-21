from backend.wallet.wallet import Wallet


def test_verify_valid_signature():
    data = {"foo": "test_data"}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert Wallet.verify(wallet.public_key, data, signature)
