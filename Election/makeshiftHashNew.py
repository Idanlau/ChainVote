from hashlib import sha256


class hasher:
    def __init__(self):
        self.inputString = ""
        self.hashString = ""

    def setInputString(self, input):
        self.inputString = input

    def __getSHA256(self, input):
        messageDigest = sha256()
        encodedInput = input.encode('utf-8')
        messageDigest.update(encodedInput)
        return messageDigest.digest()

    def __digestConvertHex(self, normalDigest):
        hexDigest = normalDigest.hex()

        return hexDigest

    def hashConvert(self):
        self.hashString = self.__digestConvertHex(self.__getSHA256(self.inputString))

    def getInputString(self):
        return self.inputString

    def getHashString(self):
        return self.hashString

    def allInOneHash(self, input):
        self.setInputString(input)
        self.hashConvert()
        return self.hashString