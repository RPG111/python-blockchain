class Block:
    """
    Block: a unit of storage.
    Store transcations in a blockchain that supports a cyrptocurrency.
    """
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f'Block - Data : {self.data}'

def main():
    block = Block('foo')
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
    main()