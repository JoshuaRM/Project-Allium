import os
from struct import pack

magic_bytes = pack('L', 3652501241)


class Blockchain:
    
    def __init__(self,filename, metadata):
        """
        Constructor that takes in a blockchain to create a copy of it
        in the class data member blockfile
        :param filename: local copy of the blockchain that will
                        be used to create this copy of the blockchain
        :no return:
        """
        self.blockfile = filename
        
        self.metadata = {
                "block_count": 0,
                "last_block": b'',
                "block_indexes": []}
        
        
        # If the file does not already exist, create the file and close it
        if not (os.path.isfile(filename)):
            with open(filename, 'wb') as f: pass
        
        if not (os.path.isfile(metadata)):
            with open(metadata, 'wb') as f: pass
        
        
        
    def add_block(self, block):
        size = get_size_bytes(self, block)
        payload = magic_bytes+size+block
        
        
        idx = os.path.getsize(self.blockfile)-1
        if idx < 0:
            idx = 0
        self.metadata["block_indexes"].append(idx)
        
        with open(self.blockfile, 'ab') as fileobj:
            fileobj.write(payload)
            
        self.metadata["last_block"] = block
        self.metadata["block_count"] += 1
        

    
def get_size_bytes(self, byteString):
    return pack('I', len(byteString))


