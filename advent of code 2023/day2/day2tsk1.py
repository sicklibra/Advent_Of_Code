#The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

def access(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line[:-1])
        line=infile.readline()
    return lnlst

def breakit(line):
    brk=line.split(': ')
    return brk

def brktohnds(hands):
    brk=hands.split('; ')
    #print(brk)
    return brk


def brkwords(line):
    brk=line.split(', ')
    
def ispossible(line):
    gamehand=breakit(line)
    hands=brktohnds(gamehand[1])
    for i in hands:
        work=figureout(i)
        if work==False:
            return False, 'a'
    gamehand=gamehand[0].split(' ')[1]
    return True, gamehand

def figureout(hand):
    hand=hand.split(', ')
    for i in hand:
        numcolor=i.split(' ')
        number=int(numcolor[0])
        color=numcolor[1]
        print(color, number)
        if color=='red':
            if number>12:
                return False
        if color=='green':
            if number>13:
                return False
        if color=='blue':
            if number>14:
                return False
    return True
        

def main():
    #file='test.txt'
    file="pastgames.txt"
    lnlst=access(file)
    print(lnlst)
    tot=0
    for i in lnlst:
        istrue, gamenum=ispossible(i)
        if istrue==True:
            print(gamenum)
            tot+=int(gamenum)
    print(tot)    

main()