from makeshiftHashNew import hasher

import json


class Block:
    hasherInstance = hasher()

    def __init__(self, index, identity, vote, timestamp, previousHash, nonce=0):
        self.index = index
        self.identity = identity
        self.vote = vote
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.nonce = nonce

    @staticmethod
    def fromDict(blockDict):
        tempBlock = Block(blockDict['index'], blockDict['identity'], blockDict['vote'], blockDict['timestamp'],
                          blockDict['previousHash'], blockDict['nonce'])
        tempBlock.hash = blockDict['hash']
        return tempBlock

    def computeHash(self):
        # This method will return the hash of whatever contents are in the block
        block_string = self.hasherInstance.allInOneHash(self.identity)
        block_string = "0" * self.nonce + block_string

        return block_string