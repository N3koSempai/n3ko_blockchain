import hashlib
import datetime
import json

from flask import Flask, jsonify

# create a main class

class Blockchain:
    
    def __init__(self):
        #ledger of chain
        self.chain = []
        
        #call function for create new block in the start (genesis)
        self.create_block(proof=1,previous_hash="0")
        
        
    def create_block(self, proof, previous_hash):
        """this function create new block usig hash to the before block and make timestamp"""
        
        block = {'index':len(self.chain)+1,
        'timestamp': str(datetime.datetime.now()),
         "proof": proof,
         "previous_hash": previous_hash}
        
        #added to chain and return actual block
        self.chain.append(block)
        return block
    
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
            if hash_operation[:12] == '000000000000':
                check_proof = True
            else:
                new_proof + 1

            return new_proof    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        result = hashlib.sha256(encoded_block).hexdigest()
        return result

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        print("fase 1")
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != '000000000000':
                return false
                
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

@app.route("/get_chain", methods=['GET'])
def get_chain():
    response = {"chain" :blockchain.chain,
    "lenght": len(blockchain.chain)}
    return jsonify(response), 200

app.run(host= '0.0.0.0', port='5000')
