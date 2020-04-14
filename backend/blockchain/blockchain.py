from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transcations.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    
    def __repr__(self):
        return f'Blockchain: {self.chain}'
    def add_block(self, data): 
        self.chain.append(Block.mine_block(self.chain[-1], data))


def main():
    blockchain = Blockchain()
    blockchain.add_block('One')
    blockchain.add_block('Two')
    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == "__main__":
    main()