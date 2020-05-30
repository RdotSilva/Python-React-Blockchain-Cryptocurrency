import requests

base_url = "http://localhost:5000"


def get_blockchain():
    return requests.get(f"{base_url}/blockchain").json()


def get_blockchain_mine():
    return requests.get(f"{base_url}/blockchain/mine").json()


start_blockchain = get_blockchain()

print(f"start_blockchain: {start_blockchain} ")
