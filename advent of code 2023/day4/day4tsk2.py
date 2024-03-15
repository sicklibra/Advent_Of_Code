"""if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards.  how many total scratchcards do you end up with?"""
import math
def openfile(filename):
    infile=open(filename,'r')
    line=infile.readline()
    lines=[]
    lastcard=0
    while line!='':
        numbers,cardnum=removenum(line[:-1])
        lines.append(numbers)
        lastcard=int(cardnum)
        line=infile.readline()

    infile.close
    #print(lastcard)
    return lines, lastcard

def removenum(line):
    num=line.split(': ')
    cardnum=num[0].split()
    #gives a reference positon so we dont go past last card. 
    cardnum=cardnum[1]
    #separates numbers to be compared in a string back to be added to list.
    num=num[1]
    return num, cardnum

def refmy(line):
    #splits list into two comparable strings
    allnum=line.split(' | ')
    #splits the first half of list into usable sub strings
    refnum=allnum[0].split()
    #splits my numbers into usable substrings. 
    mynum=allnum[1].split()

    return refnum, mynum

def getnums(cards, lastcard):
    #print(cards)
    scores=[]
    #this will track how many of each card is posesed as iteration moves forward
    numberheld=[]
    for i in range (len(cards)):
        numberheld.append(1)
    #keeps track of place in numberheld
    count=0
    for i in cards:
        playedcards=1
        refnum, mynum=refmy(i)
        #returns number of cards i won in this hand
        cards=compare(refnum, mynum, lastcard)
        print(cards)
        #adds in the number of each card held for each point score
        for f in range(cards):
            try:
                numberheld[count+f+1]+=1*numberheld[count] #consider how many extras you won off of the copies
            except:continue 

        count+=1
        lastcard-=1
    print(numberheld)
    return numberheld

def compare(refnum, mynum, lastcard):
    numcards=0
    for i in mynum:
            try:
                locate=refnum.index(i)
                if numcards<(lastcard):    
                    numcards+=1                
            except:
               continue
    return numcards
    
def main():
    file='scratchcards.txt'
    #file='sample.txt'
    cards, lastcard=openfile(file)
    tot=0
    scores=getnums(cards, lastcard)
    for i in scores:
        tot+=i

    print(tot)


main()
