# imports
import unittest
import os
from blockchain import *    
import block as B


    
class TestBlock(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain("testfile")
        
    def tearDown(self):
        os.remove("testfile")
    
    
    def test_constructor(self):
        
        filename = "testfile"
        self.assertEqual(self.bc.blockfile, filename)
        self.assertTrue(os.path.isfile(filename))
        # Opens the blockchain file and writes '0' to it
        with open(self.bc.blockfile, 'ab') as fileobj:
            fileobj.write(b'0')
        # Creates another blockchain with the same filename as test_blockchain
        test_blockchain_2 = Blockchain(self.bc.blockfile)
        # Ensures that the file of test_blockchain is not overwritten
        with open(self.bc.blockfile, 'rb') as fileobj:
            char = fileobj.read(1)
        self.assertEqual(b'0', char)
          
    def test_size(self):
        #Create a byte string to compare to
        testString = b'testing'
        #Create int byte of the length of byte string
        testLength = B.int_to_bytes(len(testString))
        #Check if int byte is equal
        self.assertEqual(get_size_bytes(self, testString), testLength)
        
    def test_add_block(self):
        target = 10**72     # Target for which all block hashes must be under
        data = B.hash_SHA("Testing block".encode())   # valid block data to be used for block construction
        prev_hash = B.hash_SHA("0".encode())
        prev_hash2 = B.hash_SHA("1".encode())
        
        bc = B.mine(prev_hash, data, target)
        bc2 = B.mine(prev_hash2, data, target)
        size = get_size_bytes(self, bc)
        self.bc.add_block(bc)
        self.bc.add_block(bc2)
        
        
        payload=read_from_file(self.bc.blockfile)
        print(bc)
        
    if __name__ == '__main__':
        unittest.main()