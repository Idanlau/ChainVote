import pandas as pd
from .voterVerifier import voterVerifierClass
from .makeshiftHashNew import hasher


class initVoters:
    def __init__(self):
        self.initHasher = hasher()

        # windows:
        self.verifVals = pd.read_csv(r"/Users/idanlau/ChainVote/ChainVote/Election/globalVals.csv")
        self.votersDf = pd.read_csv(
            r"/Users/idanlau/ChainVote/ChainVote/Election/registeredVoters.csv")

        # macOS:
        # self.verifVals = pd.read_csv("/Volumes/Vikram's Hard Drive/Programming/chainVote/globalVals.csv")
        # self.votersDf = pd.read_csv("/Volumes/Vikram's Hard Drive/Programming/chainVote/voterInformation/registeredVoters.csv")

        # Setting up date for dob
        self.votersDf.insert(loc=len(self.votersDf.columns), column="Hash", value="hash")
        self.votersDf = self.votersDf.astype({'Date of Birth': 'datetime64[ns, US/Eastern]'})
        self.votersDf['Date of Birth'] = self.votersDf['Date of Birth'].dt.date

        self.voterVerificationSystem = voterVerifierClass(self.verifVals)

        self.votersDf['Hash'] = 'tempHash'

        for index, voter in self.votersDf.iterrows():
            preHash = self.voterVerificationSystem.processVoter(voter)
            print(preHash)
            postHash = self.initHasher.allInOneHash(preHash)
            self.votersDf.loc[self.votersDf['First Name'] == voter.loc['First Name'], 'Hash'] = postHash

        print(self.votersDf['Hash'])

        approvedHashes = self.votersDf['Hash']
        approvedHashes.to_csv(r"/Users/idanlau/ChainVote/ChainVote/Election/approvedHash.csv",
                              index=0)

