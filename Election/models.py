from django.db import models
from .makeshiftHashNew import hasher
# Create your models here.
from .initVoters import initVoters
from .globalValsGenerator import run

class Election(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    run()
    initVoters()

    def save(self, *args, **kwargs):
        #run()
        # initVoters()
        super(Election, self).save(*args, **kwargs)


class Candidates(models.Model):
    election = models.ForeignKey(Election, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=1000)
    vote_count = models.IntegerField(default=0)

class Block(models.Model):
    election = models.ForeignKey(Election, on_delete = models.CASCADE)
    index = models.IntegerField()
    identity = models.CharField(max_length=1000000)
    vote = models.IntegerField()
    timestamp = models.DateTimeField()
    previousHash = models.CharField(max_length=1000000)
    nonce = models.IntegerField()

    def save(self, *args, **kwargs):
        hasherInstance = hasher()
        new_idd = str(self.identity) + str(self.vote) + str(self.timestamp)
        self.identity = hasherInstance.allInOneHash(new_idd)
        print(new_idd)

        super(Block, self).save(*args, **kwargs)



    def proofOfWork(self, hash):
        # hasherInstance = hasher()
        difficulty = 0
        # This method goes through values of nonce until it gets a hash satisfying the difficulty we set

        self.nonce = 0

        # computedHash = block.computeHash()

        while not hash.startswith('0' * difficulty):
            self.nonce += 1
            self.identity = Block.computeHash(self,hash)
            hash = self.identity
        return hash

    def computeHash(self, idd):
        # This method will return the hash of whatever contents are in the block

        block_string = "0" * self.nonce + idd

        return block_string

class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete = models.CASCADE)
    index = models.IntegerField()
    identity = models.CharField(max_length=1000000)
    vote = models.IntegerField()
    timestamp = models.DateTimeField()
    previousHash = models.CharField(max_length=1000000)
    nonce = models.IntegerField()

    def save(self, *args, **kwargs):
        hasherInstance = hasher()
        new_idd = str(self.identity) + str(self.vote)
        self.identity = hasherInstance.allInOneHash(new_idd)
        super(Vote, self).save(*args, **kwargs)

class PrevHash(models.Model):
    election = models.OneToOneField(Election, null=True, on_delete=models.CASCADE)
    identity = models.CharField(max_length=1000000)

class RealPrevHash(models.Model):
    election = models.OneToOneField(Election, null=True, on_delete=models.CASCADE)
    identity = models.CharField(max_length=1000000)






