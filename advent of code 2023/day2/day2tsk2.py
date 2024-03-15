#what is the minimum number of cubes that can make a hand. 
'''what i need to do.
find the max of each color for each game. 
multiply the max of each color by eachother 
then for each game, add the total. '''

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
    
def getnum(line):
    gamehand=breakit(line)
    hands=brktohnds(gamehand[1])
    gametot=figureout(hands)
    return gametot

def figureout(hands):
    red, green, blue=0,0,0
    for i in hands:
        hand=i.split(', ')    
        for f in hand:
            numcolor=f.split(' ')
            number=int(numcolor[0])
            color=numcolor[1]        
            if color=='red':
                if number>red:
                    red=number
            if color=='green':
                if number>green:
                    green=number
            if color=='blue':
                if number>blue:
                    blue=number
    #print(red, green, blue)
    gametot=blue*red*green
    return gametot 
        

def main():
    """file=test.txt"""
    file="pastgames.txt"
    lnlst=access(file)
    #print(lnlst)
    tot=0
    for i in lnlst:
        gametot=getnum(i)
        tot+=int(gametot)
    print(tot)    

main()