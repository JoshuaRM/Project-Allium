import os.path
from struct import pack

magic_bytes = pack('L', 3652501241)


class Blockchain:
    
    def __init__(self,filename):
        """
        Constructor that takes in a blockchain to create a copy of it
        in the class data member blockfile
        :param filename: local copy of the blockchain that will
                        be used to create this copy of the blockchain
        :no return:
        """
        self.blockfile = filename
        # If the file does not already exist, create the file and close it
        if not (os.path.isfile(filename)):
            with open(filename, 'wb') as f: pass
        
    def add_block(self, block):
        size = get_size_bytes(self, block)
        payload = magic_bytes+size+block
        
        with open(self.blockfile, 'ab') as fileobj:
            fileobj.write(payload)

    
def get_size_bytes(self, byteString):
    return pack('I', len(byteString))

def read_from_file(filename: str):
    payload=[]
    with open(filename, 'rb') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            payload.append(char)
    
    return payload

