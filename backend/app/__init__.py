from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

for i in range(3):
    blockchain.add_block(i)

@app.route('/')
def route_default():
    return 'Welcome to the blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

app.run()