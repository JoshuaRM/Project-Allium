# imports
import unittest
import os
from blockchain import *    
import block as B


    
class TestBlock(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain("testfile", "metadata.json")
        
    def tearDown(self):
        os.remove("testfile")
        os.remove("metadata.json")
    
    
    def test_constructor(self):
        
        filename = "testfile"
        metadata = "metadata.json"
        self.assertEqual(self.bc.blockfile, filename)
        self.assertTrue(os.path.isfile(filename))
        # Opens the blockchain file and writes '0' to it
        with open(self.bc.blockfile, 'ab') as fileobj:
            fileobj.write(b'0')
        # Creates another blockchain with the same filename as test_blockchain
        test_blockchain_2 = Blockchain(self.bc.blockfile, metadata)
        # Ensures that the file of test_blockchain is not overwritten
        with open(self.bc.blockfile, 'rb') as fileobj:
            char = fileobj.read(1)
        self.assertEqual(b'0', char)
        
        #For testing metadata structure
        block_indexes = test_blockchain_2.metadata["block_indexes"]
        block_count = test_blockchain_2.metadata["block_count"]
        last_block = test_blockchain_2.metadata["last_block"]
        
        self.assertEqual(0, block_count)
        self.assertEqual(b'', last_block)
        self.assertEqual([], block_indexes)
          
    def test_size(self):
        #Create a byte string to compare to
        testString = b'testing'
        #Create int byte of the length of byte string
        testLength = B.int_to_bytes(len(testString))
        #Check if int byte is equal
        self.assertEqual(get_size_bytes(self, testString), testLength)
        
    def test_add_block(self):
        target = 10**72     
        data = B.hash_SHA("Testing block".encode())   
        prev_hash = B.hash_SHA("0123456789ABCDEF".encode())
        
        #Create a block using .mine()
        bc = B.mine(prev_hash, data, target)
        #Get size of block
        size = get_size_bytes(self, bc)
        # Add block to blockchain
        self.bc.add_block(bc)
        
        
    if __name__ == '__main__':
        unittest.main()