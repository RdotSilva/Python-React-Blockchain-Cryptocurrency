import requests


def get_blockchain():
    return requests.get("http://localhost:5000/blockchain").json()


start_blockchain = get_blockchain()

print(f"start_blockchain: {start_blockchain} ")
