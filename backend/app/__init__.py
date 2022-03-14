import os
import random

from flask import Flask, jsonify

from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pub_sub = PubSub()

for i in range(3):
    blockchain.add_block(i)


# ASDfghjkl1234567890!
@app.route('/')
def default():
    return 'Welcome to blockchain \'HJL\''


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pub_sub.broadcast_block(block)

    return jsonify(block.to_json())


PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

app.run(port=PORT)
