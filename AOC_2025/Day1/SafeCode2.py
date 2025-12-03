'''Day 1 Advent of code 2025
Author: Josh Hodges

The text file in this is arranged with a letter followed by a number. These are in reference to a dial that reads
from 0-99. The number is how many 'clicks' the dial is to be turned and the letter is what direction. 
the final result is a count of how many times the dial lands on 0 '''

'''read the file to array containing the letter and number '''

def readFile(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line.strip('\n'))
        line=infile.readline()
    return lnlst

'''Okay, now i have to count all of the times the dial =0 this should be relatively easy. I will simply use floor division on the final result and with the
negatives simply add another to the count.'''
def main():
    # lns=readFile('test.txt')
    lns = readFile('./day1_input.txt')
    count=0
    #dial starts at 50
    dial=50
    for i in lns:
        if dial%100 == 0:
            dial=0
            count+=1     
        if len(i)==2:
            num=int(i[-1])
        else:
            num=int(i[1:])
        dir=i[0]
        '''Alright, done being clever, it came out more complicated than it needed to be for the purposes of this exercise... Brute force it is. '''
        print(dial, dir, num, count)
        if dir=='R':
            for j in range (num): 
                if dial == 100:
                    count+=1
                    dial = 0
                dial+=1
        else:
            for j in range (num):
                if dial == 0:
                    if j!= 0:
                        count+=1
                    dial=100
                dial-=1

        
    print(count)

main()
