import sys
import random
from math import sqrt

WIDTH = 1024
HEIGHT = 600

def checkTargets(theTargets,sizeTarget,minSpace,x,y):
    res = True
    i = 0
    while i != len(theTargets) and res:
        currentTarget = theTargets[i]
        i += 1
        dist = sqrt( (x-currentTarget[0])**2 + (y-currentTarget[1])**2 )
        if dist-sizeTarget < minSpace:
            res = False
    return res


def placeTarget(theTargets,sizeTarget,minSpace):
    x = random.randint(0,WIDTH-minSpace)
    y = random.randint(0,HEIGHT-minSpace)
    while not(checkTargets(theTargets,sizeTarget,minSpace,x,y)):
        x = random.randint(0,WIDTH-minSpace)
        y = random.randint(0,HEIGHT-minSpace)
    return (x,y)

def createFiles(nbTargets,sizeTarget,minSpace):
    ext = str(nbTargets)+'_'+str(sizeTarget)+'_'+str(minSpace)+'.csv'
    ciblename = './media/terrains/cibles_'+ext
    sequencename = './media/sequences/sequence_'+ext
    createCibles(ciblename,nbTargets,sizeTarget,minSpace)
    createSequence(sequencename,nbTargets)
    

def createCibles(filename,nbTargets,sizeTarget,minSpace):
    theTargets = []
    with open(filename, 'w') as f:
        for _ in range(nbTargets):
            line = placeTarget(theTargets,sizeTarget,minSpace)
            theTargets.append(line)
            f.write(str(line[0])+','+str(line[1])+','+str(sizeTarget))
            f.write('\n')

def createSequence(filename,nbTargets):
    sequence = [str(i) for i in range(nbTargets)]
    random.shuffle(sequence)
    with open(filename, 'w') as f:
        for i in sequence:
            f.write(i)
            f.write('\n')

def main(args):
    if len(args) != 4:
        print("Not enough parameters ! Please use python3 CreateTargets.py nbTargets sizeTarget minSpace")
    else:
        nbTargets = int(args[1])
        sizeTarget = int(args[2])
        minSpace = int(args[3])
        createFiles(nbTargets,sizeTarget,minSpace)


if __name__ == "__main__":
    main(sys.argv)