import pandas as pd


class voterVerifierClass:
    def getDobNum(self, ogValue, index):
        try:
            return int(ogValue[index])
        except:
            return 0

    def __init__(self, idVals):
        self.verifVals = idVals
        # Initializing all values

        self.fNameStart = self.verifVals["fNameStart"][0]
        self.fNameLen = self.verifVals["fNameLen"][0]

        self.lNameStart = self.verifVals["lNameStart"][0]
        self.lNameLen = self.verifVals["lNameLen"][0]

        self.dobM = self.verifVals["dobM"][0]
        self.dobMModifier = self.verifVals["dobMModifier"][0]
        self.dobD = self.verifVals["dobD"][0]
        self.dobDModifier = self.verifVals["dobDModifier"][0]
        self.dobOverallModifier = self.verifVals["dobOverallModifier"][0]

        self.idStart = self.verifVals["idStart"][0]
        self.idLen = self.verifVals["idLen"][0]

        self.pnStart = self.verifVals["pnStart"][0]
        self.pnLen = self.verifVals["pnLen"][0]

    def processVoter(self, voterInfo):
        returnString = ""
        returnString += str(str(voterInfo['First Name'])[self.fNameStart: self.fNameStart + self.fNameLen])
        returnString += str(str(voterInfo['Last Name'])[self.lNameStart: self.lNameStart + self.lNameLen])

        dobAdder = voterInfo['Date of Birth'].year
        dobAdder += self.getDobNum(str(voterInfo['Date of Birth'].month), self.dobM) * self.dobMModifier
        dobAdder += self.getDobNum(str(voterInfo['Date of Birth'].day), self.dobD) * self.dobDModifier
        dobAdder += self.dobOverallModifier

        returnString += str(dobAdder)
        returnString += str(str(voterInfo['Identification'])[self.idStart: self.idStart + self.idLen])
        returnString += str(str(voterInfo['Phone Number'])[self.pnStart: self.pnStart + self.pnLen])

        return returnString