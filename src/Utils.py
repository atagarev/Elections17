from Objects import CountPerMIR

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
    print("Total of {} lines".format(lines.__len__()))
    mandates = None
    totals = None
    parties = dict()
    for line in lines:
        cols = line.split("\t")
        if cols[0] == "Party":
            print("Encountered header row with {} columns".format(len(cols)))
        elif cols[0] == "Total Votes":
            print("Encountered total votes with {} columns.".format(len(cols)))
            totals = CountPerMIR("Votes", cols[33], cols[1:33])
            totals.getCountTotal()
        elif cols[0] == "Total Mandates":
            print("Encoutered total mandates with {} columns.".format(len(cols)))
            mandates = CountPerMIR("Mandates", cols[33], cols[1:33])
        else:
            print("Encountered row for party {} with {} collumns".format(cols[0], len(cols)))
            parties[cols[0]] = CountPerMIR(cols[0], cols[33], cols[1:33])
    return mandates, totals, parties

def calculateSupportThreshold(totals):
    if type(totals) != CountPerMIR:
        raise ValueError("Unexpected input type encountered.")
    return totals.getCountTotal()*0.01

def calculateEntryThreshold(totals):
    if type(totals) != CountPerMIR:
        raise ValueError("Unexpected input type encountered.")
    return totals.getCountTotal()*0.04

def calculateMandateQuota()

readMIRMandates()
readFullVotes()