class CountPerMIR():

    def __init__(self, name, total, perMIR):
        self.name = name
        self.countTotal = total
        self.countsPerMIR = perMIR

    def getName(self):
        return self.name

    def getCountTotal(self):
        return self.countTotal

    def getVotesInMIR(self, mir):
        if type(mir) != int or mir > len(self.countsPerMIR) or mir <= 0:
            raise ValueError("Invalid MIR number {} was requested.".format(mir))
        return self.countsPerMIR[mir]

class CountPerParty():

    def __init__(self, perParty):
        for count in perParty.values()
        self.countTotal = total