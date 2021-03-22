

def readFile(filename):
    lines = []
    with open(filename, encoding="utf-8") as f:
        for l in f:
            lines.append(l.strip())
    return lines

def readMIRMandates():
    print('Blyah')

def readFullVotes():
    lines = readFile("../data/VotesPerPartyPerMIR.tsv")
    print("Total of %s lines".format(lines.__len__()))

readMIRMandates()
readFullVotes()