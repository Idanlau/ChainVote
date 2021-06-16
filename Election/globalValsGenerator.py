import random
import pandas as pd

def run():
    dfDict = {
        'fNameStart' : random.randint(0, 3),
        'fNameLen' : random.randint(4, 8),
        'lNameStart' : random.randint(0, 3),
        'lNameLen' : random.randint(4, 6),
        'dobM' : random.randint(0,1),
        'dobMModifier' : random.randint(1,100),
        'dobD' : random.randint(0,1),
        'dobDModifier' : random.randint(1,100),
        'dobOverallModifier' : random.randint(0,7500),
        'idStart' : random.randint(0, 3),
        'idLen' : random.randint(2, 6),
        'pnStart' : random.randint(0, 4),
        'pnLen' : random.randint(3, 8)
    }

    importantVals = pd.DataFrame(dfDict, index = [0])

    # windows
    importantVals.to_csv(r"/Users/idanlau/ChainVote/ChainVote/Election/globalVals.csv", index = [0])
    # mac
    # importantVals.to_csv("/Volumes/Vikram's Hard Drive/Programming/chainVote/globalVals.csv", index = None)