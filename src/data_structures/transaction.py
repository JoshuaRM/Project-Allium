from block import hash_SHA, long_to_bytes, short_to_bytes, bytes_to_short, bytes_to_long
import ecdsa
from collections import deque


def create_output(value, recipient):
    """
    Convert the value to a long and concatenate it with the recipient

    :param value: value of transaction
    :param recipient: recipient of transaction
    :return: concatenation of the value converted to a long and the recipient 
    """
    return long_to_bytes(value) + recipient

def sign_transaction(private_key, prev_tx_hash, prev_tx_locking_script, new_tx_output):
    """
    Signs a transaction hash

    :param private_key: users private key
    :param prev_tx_hash: hash to the previous transaction
    :param prev_tx_locking_script: locking script to the previous transaction
    :param new_tx_hash: the hash of the current transaction
    :return: signature of the unsigned transaction hash
    """
    # concatenation of all keys except private key
    concat = prev_tx_hash + prev_tx_locking_script + new_tx_output
    # hashes the concatenated keys
    unsigned_tx_hash = hash_SHA(concat)
    # creates signing key
    signing_key = ecdsa.SigningKey.from_string(private_key,curve=ecdsa.SECP256k1)
    # signs the hashed transaction
    return signing_key.sign(unsigned_tx_hash)


def create_input(previous_tx_hash, index, signature, public_key):
    """
    Creates transation input

    :param previous_tx_hash: hash of the previous transaction
    :param index: Index of output
    :param signature: signature of the transaction hash
    :param public_key: users public key
    :return: concatenation of parameters with the index changed to a short
    """
    unlocking_script = signature + public_key
    index_short = short_to_bytes(index)
    return previous_tx_hash + index_short + unlocking_script

def parse_input(input):
    """
    Parses transaction input into dictionary

    :param input: Transaction input
    :return: dictionary containing transaction input parameters
    """
    # Create empty dictionary
    parsed_input = {}
    # Parse out sections of input into dictionary values
    parsed_input["previous_tx_hash"] = input[0:32]
    parsed_input["index"] = bytes_to_short(input[32:34])
    parsed_input["signature"] = input[34:98]
    parsed_input["public_key"] = input[98:162]
    # Return the dictionary
    return parsed_input

def parse_output(output):
    """
    Parses transaction output into dictionary

    :param output: Transaction output
    :return: dictionary containing transaction output parameters
    """
    # Create empty dictionary
    parsed_output = {}
    # Parse out sections of output into dictionary values
    parsed_output["value"] = bytes_to_long(output[0:4])
    parsed_output["recipient"] = output[4:36]
    # Return the dictionary
    return parsed_output
