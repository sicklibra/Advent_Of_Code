'''
Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only.


Problem:
The text file is an amalgomation of characters. and my job is to find how many times xmas appears. i will do this based off of the x's as the beginning character. by breaking each line into a list of lists. with this i will be able to monitor and adjust accordingly. steps:
1)create list of lists of each line. 
2)simply find each "XMAS" and "SAMX"
3)Iterate through each list looking for X
    Xfound rules:
    A) if the index of list being used is <3 ignore looking up (out of bounds error and wont
        find it anyway)
    B)if index of list is > len(list)-4 ignore looking down (out of bounds and not enough space)
    C)if x is found not withstanding rules abovefirst check list up ref above lists, then check down, then check diagonal up back, down forward, and up forward (if index of x is <3 dont check back, if index of x is len(list)-4) dont check forward'''
'''Problem 2:
this problem should be easy to solve in roughly the same way as the last one. I am to be identifying mas in the shape of an x
m.m   s.s   m.s   s.m
.a.   .a.   .a.   .a.
s.s   m.m   m.s   s.m
The common denominator here is that an A must be in the middle so:
    1) Starting at line 1(not 0) i will scan each line for an "A"from pos 1 to pos len(lst)-2(leaves
        a gap at the end)
    2) When an A is identified, the counter will look at the line before first for a pattern:
        (i-1==m and i+1==m) or(m/s) or(s/m) or (s/s) this will identify the potential
        in the subclause of each if statement, embed the relevant corrisponding character order for the line below'''


def accessfile(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line[:-1])
        line=infile.readline()
    return lnlst

def countXMAS(lines):
    count=0
    for line in lines:
        lineind=lines.index(line)
        if lineind>0 and lineind<len(lines)-1:
            for i in range(len(line)-1):
                if i==0:
                    continue
                else:
                    if line[i]=="A":
                        count+=checkA(lines, lineind, i)
    print(count)


def checkA(lines, line, A):
    topL=lines[line-1][A-1]
    topR=lines[line-1][A+1] 
    botL=lines[line+1][A-1]
    botR=lines[line+1][A+1]
    if topL=="M" and topR=="M":
        if botL=="S" and botR=="S":
            return 1
        else:
            return 0
    elif topL=="S" and topR=="S":
        if botL=="M" and botR=="M":
            return 1
        else:
            return 0
    elif topL=="S" and topR=="M":
        if botL=="S" and botR=="M":
            return 1
        else:
            return 0
    elif topL=="M" and topR=="S":
        if botL=="M" and botR=="S":
            return 1
        else:
            return 0
    else:
        return 0


def main():
    test2='test2.txt'
    test='WordsearchTest.txt'
    file='Wordsearch.txt'
    lines=accessfile(file)
    countXMAS(lines)

main()
