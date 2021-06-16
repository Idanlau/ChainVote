from django.shortcuts import render
from .models import Candidates,Election,Block,Vote,PrevHash
from django.views.generic import ListView
from .makeshiftHashNew import hasher
from datetime import datetime
import numpy as np

from .voterVerifierNew import voterVerifierClass1

import pandas as pd
from .initVoters import initVoters
# Create your views here.

def election_view(request,id):
    election = Election.objects.get(id=id)
    candidate = Candidates.objects.filter(election=election)
    candidate1 = candidate.first()
    candidate2 = candidate.last()
    b = Block.objects.filter(election=election)

    hasherInstance = hasher()
    verifVals = pd.read_csv(r"/Users/idanlau/ChainVote/ChainVote/Election/globalVals.csv")
    vote_verify = voterVerifierClass1(verifVals)






    if request.method == 'POST':

        if request.POST.get('option') == '1':
            candidate1.vote_count += 1

        elif request.POST.get('option') == '2':
            candidate2.vote_count += 1

        ori_idd_dict = {
            'First Name' : str(request.POST.get('f_name')),
            'Last Name': str(request.POST.get('l_name')),
            'Date of Birth': str(request.POST.get('DOB')),
            'Identification':str(request.POST.get('id')),
            'Phone Number': str(request.POST.get('p_number'))
        }

        votersDf = pd.DataFrame(ori_idd_dict, index=[0])
        print(votersDf)
        # votersDf['Date of Birth New'] = pd.to_datetime(votersDf['Date of Birth'])
        #votersDf['timestamp'] = pd.to_datetime(votersDf['timestamp'])

        votersDf = votersDf.astype({'Date of Birth': 'datetime64[ns, US/Eastern]'})
        # votersDf['Date of Birth'] = votersDf['Date of Birth'].dt.date
        votersDf['Date of Birth'] = pd.to_datetime(votersDf['Date of Birth'], format = '%d/%m/%Y')
        votersDf['Date of Birth'] = pd.to_datetime(votersDf['Date of Birth'], format='%d/%m/%Y')

        print(votersDf)
        print("NEW PRINT")
        print("NEW PRINT")
        print("NEW PRINT")
        print("NEW PRINT")


        print(type(votersDf['Date of Birth']))


        for index, voter in votersDf.iterrows():
            stringToHash = vote_verify.processVoter(voter)
        print(stringToHash)
        idd = hasherInstance.allInOneHash(stringToHash)

        #
        # ori_idd = pd.df[]
        # idd = hasherInstance.allInOneHash(ori_idd)


        previousHash = b.last().identity
        print(idd)
        # vote_verify.processVoter(ori_idd)
        print('error')
        u=Block.objects.create(election = election, index = 0, identity = idd, vote=int(request.POST.get('option')),timestamp = datetime.now(),
                            previousHash=previousHash, nonce=0)

        print(u)
        ph = PrevHash.objects.filter(election=election)
        ph = ph.last()
        print(ph.identity)
        print(u.previousHash)


        if ph.identity == u.previousHash:
            # u.save()
            Sec =  check_prev(b,u.previousHash)
            if Sec == True:
                print('pass')
                # ph.save()
                if isValidProof(Block, u.identity):
                    u.save()

                    candidate1.save()
                    candidate2.save()
                    ph.identity = u.identity
                    ph.save()
                #
                # else:
                #     u.delete()

                else:
                    print(u.identity)
                    print('Not valid user')
                    u.delete()







            else:
                u.delete()
                print('invalid all blocks')

        else:
            print('invalid')
            u.delete()







    return render(request, "ElectionView.html", {'candidate':candidate,
                                                 'candidate1':candidate1,'candidate2':candidate2})

def check_prev(b,PrevHash):
    for i in range(1, len(b)):
        if b[i].previousHash != b[i - 1].identity:
            for m in range(i-1,len(b)):
                b[m].delete()
            PrevHash.identity = 0
            PrevHash.save()
            return False
    return True

def proofOfWork(block,hash):
    #hasherInstance = hasher()
    difficulty = 0
        # This method goes through values of nonce until it gets a hash satisfying the difficulty we set

    block.nonce = 0

    #computedHash = block.computeHash()

    while not hash.startswith('0' * difficulty):
        block.nonce += 1
        block.identity = computeHash(block,hash)
        block.save()
        hash = block.identity
    return hash

def isValidProof(block, blockHash):
    difficulty = 0
        # Method to check if blockHash is a valid hash of block
    checking = True
    approvedIdentities = np.genfromtxt('/Users/idanlau/ChainVote/ChainVote/Election/approvedHash.csv', delimiter=',',
                                       dtype=None)
    print(approvedIdentities)

    #for i in approvedIdentities:
    # if blockHash == '0' * difficulty + i.decode("utf-8"):
    #     checking = True



    return (blockHash.startswith('0' * difficulty) and checking)

def computeHash(block,idd):
    # This method will return the hash of whatever contents are in the block
    print(idd)
    block_string = "0" * block.nonce + idd

    return block_string