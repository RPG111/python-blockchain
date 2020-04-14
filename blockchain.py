class Block:
    """
    Block: a unit of storage.
    Store transcations in a blockchain that supports a cyrptocurrency.
    """
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'Block - Data : {self.data}'
class Blockchain:
    """
    Blockchain: a public ledger of transcations.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = []         
    
    def __repr__(self):
        return f'Blockchain: {self.chain}'
    def add_block(self, data):  
        self.chain.append(Block(data))

blockchain = Blockchain()
blockchain.add_block('One')
blockchain.add_block('Two')

print(blockchain)