from .makeshiftHashNew import hasher
from .block import Block
import time
import numpy as np


class Blockchain:
    # Setting up how difficult our proof of work algorithm is
    difficulty = 2
    approvedIdentities = np.genfromtxt(
        '/Volumes/Vikram\'s Hard Drive/Programming/chainVote/voterInformation/approvedHash.csv', delimiter=',',
        dtype=None)
    print(approvedIdentities)
    stringTest = "bc0a049f17cc70d95f5af18552cc4961898ca671bf78f2668294dc26033e3d9b"
    print(approvedIdentities[1].decode("utf-8") == stringTest)

    def __init__(self): # done
        self.unconfirmedTransactions = []
        self.chain = []

        # User validations, sort of like an 'account'
        self.openSurveys = {}

        # Setting up the smart contracts
        self.chainCode = {'chain': self.chain,
                          'open_surveys': self.openSurveys,
                          'unconfirmed_transactions': self.unconfirmedTransactions}

        self.createGenesisBlock()

    @staticmethod
    def fromList(chain): #done
        blockchain = Blockchain()
        blockchain.unconfirmedTransactions = []

        for block in chain:
            blockchain.chain.append(Block.fromtDict(block))

        return blockchain

    def createGenesisBlock(self): #done
        # Method to make the first block of the block chain (genesis block)

        genesisBlock = Block(0, "master", [], time.time(), "0")

        # First initiation proof of work
        self.proofOfWork(genesisBlock)

        genesisBlock.hash = genesisBlock.computeHash()

        self.chain.append(genesisBlock)

    @property
    def lastBlock(self): #done
        return self.chain[-1]

    def addBlock(self, block, proof): #half done

        # This method adds to the blockchain after verifying PoW and
        # Ensuring previousHash in the block is the same as the newest block in the chain

        previousHash = self.lastBlock.hash

        if previousHash != block.previousHash:
            return False

        if not Blockchain.isValidProof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def proofOfWork(self, block): # solving
        # This method goes through values of nonce until it gets a hash satisfying the difficulty we set

        block.nonce = 0

        computedHash = block.computeHash()

        while not computedHash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computedHash = block.computeHash()

        return computedHash

    def addNewTransaction(self, transaction): #implemented
        self.unconfirmedTransaction.append(transaction)

    @classmethod
    def isValidProof(self, block, blockHash):
        # Method to check if blockHash is a valid hash of block
        checking = False



        for i in approvedIdentities:
            if blockHash == '0' * Blockchain.difficulty + approvedIdentities[1].decode("utf-8"):
                checking = True
                break

        return (blockHash.startswith('0' * Blockchain.difficulty) and checking)

    @classmethod
    def check_chain_validity(self, chain): #
        result = True
        previousHash = "0"

        for block in chain:
            blockHash = block.hash

            delattr(block, "hash")

            if not cls.isValidProof(block, blockHash) or previousHash != block.previousHash:
                result = False
                break

            block.hash, previousHash = blockHash, blockHash

        return result


blockchainTest = Blockchain()
print("everything working")