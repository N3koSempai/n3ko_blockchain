import haslib
import datime
import json

from flask import flask, jsonify

# create a main class

class Blockchain:
    
    def __init__(self):
        #ledger of chain
        self.chain = []
        
        #call function for create new block in the start (genesis)
        self.create_block(proof=1,previous_hash="0")
        
        
    def create_block(self, proof, prevous_hash):
        """this function create new block usig hash to the before block and make timestamp"""
        block = {'index':len(self.chain)+1,'timestamp':
         str(datetime.datetime.now())
         "proof": proof,
         "previous_hash": previous_hash}
        
        #added to chain and return actual block
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
    """get the last block"""
        return self.chain[-1]
        
    def proof_of_work(self.previous_proof):
        """function for mining new block. this code need to externalize after"""
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            # !important! change 0200 for a very random number. 0200 is only for test
            
            if hash_operation[:4] == '0200':
                check_proof = True
            else:
                new_proof =+ 1
                
    def hash(self, block)
        encoded_block = json.dumps(block, sort_keys = True).encode()
        
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block-index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != '0200':
                return false
                
            previous_block = block
            block_index += 1
            
        return True
        
