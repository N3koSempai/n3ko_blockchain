

# create by Alvaro @nekosempai


import hashlib
import datetime
import json

from flask import Flask, jsonify, request



import requests
from uuid import uuid4
from urllib.parse import urlparse

# create a main class

class Blockchain:
    
    def __init__(self):
        #ledger of chain
        self.chain = []
        #block for transaction detail
        self.transaction = []
        #call function for create new block in the start (genesis)
        self.create_block(proof=1,previous_hash="0")
        #
        self.node = set()
    
    
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.node.add(parsed_url.netloc)
    
    def replace_chain(self):
        network = self.node
        longest_chain = None
        max_length = len(self.chain)
        #scanning node in network
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()
                print(length)
                length = length['length']
                chain = response.json()
                chain = chain['chain']
                
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
            if longest_chain:
                self.chain = longest_chain
                return True
            return False
                
    def create_block(self, proof, previous_hash):
        """this function create new block usig hash to the before block and make timestamp"""
        
        block = {'index':len(self.chain)+1,
        'timestamp': str(datetime.datetime.now()),
         "proof": proof,
         "previous_hash": previous_hash,
         'transaction': self.transaction}
        self.transaction = []
        #added to chain and return actual block
        self.chain.append(block)
        return block
    
    def add_transaction(self, sender, receiver, amount):
        """create the transaction block"""
        self.transaction.append({'sender': sender,'receiver': receiver,
                                'amount': amount })
        previous_block = self.get_previous_block()
        return previous_block['index'] +1 
        
    
    def get_previous_block(self):
        """get the last block"""
        return self.chain[-1]
        
    def proof_of_work(self, previous_proof):
        """function for mining new block. this code need to externalize after"""

        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # !important! change 0200 for a very random number. 0200 is only for test    
            print(hash_operation)
            if hash_operation[:4] == '0000':
                check_proof = True
                print(check_proof)
            else:
                new_proof += 1
        return new_proof   

    def hash(self, block):
        """create a hash of the block"""
        encoded_block = json.dumps(block, sort_keys = True).encode()
        result = hashlib.sha256(encoded_block).hexdigest()
        return result

    def is_chain_valid(self, chain):
        """test if all the chain is valid 'experimental'"""
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):

                return False
            previous_proof = previous_block['proof']
            #this part have a error. need better algorithm
            proof = block['proof']
            new_proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != '0000':
                return False
                
            previous_block = block
            block_index += 1
            
        return True

app = Flask(__name__)
blockchain = Blockchain()


# endpoint for mining a new block
@app.route("/mine_block", methods=['GET'])
def mine_block():
    
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']

    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)

    block = blockchain.create_block(proof,previous_hash)
    
    response = {"message": "congratulations, you mined a block",
    "index": block["index"],
     "timestamp": block["timestamp"],
      "proof": block["proof"],
       "previous_hash":block["previous_hash"]}
    
    return jsonify(response), 200

#endpoint for get the blockchain
@app.route("/get_chain", methods=['GET'])
def get_chain():
    response = {"chain" :blockchain.chain,
    "length": len(blockchain.chain)}
    return jsonify(response), 200



#endpoint for check the blockchain
@app.route("/is_valid", methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {"message": "all ok"}
        return jsonify(response), 200
    else:
        
        response = {"message": "!the blockchain is not valid!",
                    "debug_info": is_valid}
    
        return jsonify(response), 404

#
@app.route("/add_trans", methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all (key in json for key in transaction_keys):
        return "error some element are not in the array", 400
    index = blockchain.add_transaction(json['sender'], json['receiver'],json['amount'])
    response = {'message': f'the transaction was added to the block {index}'}
    return jsonify(response), 201
    
    
#connecting new nodes
@app.route("/connect_node", methods=['POST'])
def connect_node():
    print(1)
    print(request.get_json())
    json = request.get_json()
    print(json)
    print('ok')
    nodes = json.get('nodes')
    print('get_node')
    if nodes is None:
        return "no node", 401
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All nodes are connected. N3ko Blockchain have this nodes', 'total_nodes': list(blockchain.node)}
    return jsonify(response), 201


# remplacing the chain for the most large
@app.route("/replace_chain", methods=['GET'])
def replace_chain():
    is_chain_replace = blockchain.replace_chain()
    if is_chain_replace:
        response = {"message": "the chain are replacing with the most large", "new_chain": blockchain.chain}
        return jsonify(response), 200
    else:
        
        response = {"message": "this chain is already the most large",
                    "actual_chain": blockchain.chain}
    
        return jsonify(response), 200
    
app.run(host= '0.0.0.0', port='5001 ')
