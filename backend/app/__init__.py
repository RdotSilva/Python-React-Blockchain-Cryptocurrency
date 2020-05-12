from flask import Flask

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()


@app.route("/")
def route_default():
    return "Welcome to the blockchain"


@app.route("/blockchain")
def route_blockchain():
    return blockchain.__repr__()


app.run()
