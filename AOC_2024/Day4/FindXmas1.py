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

import re

def accessfile(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line[:-1])
        line=infile.readline()
    return lnlst

def countXMAS(lines):
    count=getStraights(lines)
    count+=getVerticals(lines)
    count+=getDiagonals(lines)
    print(count)


def getStraights(lines):
    count=0    
    for line in lines:
        # print(count)
        i=0
        j=0
        while (i>=0):
            i=line.find('XMAS',i, len(line))            
            if i>=0:
                count+=1
                i+=1
        while (j>=0):
            j=line.find('SAMX', j, len(line))
            if j>=0:
                count+=1
                j+=1
                # if i>len(line)-3:
                #     i=-1
    return count

def getVerticals(lines):
    count=0
    for line in lines:
        lineindex=lines.index(line)
        for i in range(len(line)):
            if line[i]=="X":
                if lineindex<3:
                    count+=getDown(lines, lineindex, i)
                elif lineindex>=len(line)-3:
                    count+= getUp(lines, lineindex, i)
                else:
                    count+=getDown(lines, lineindex, i)
                    count+=getUp(lines, lineindex, i)                
    return count

def getDiagonals(lines):
    count=0
    for line in lines:
        lineindex=lines.index(line)
        for i in range(len(line)):
            if line[i]=="X":
                #cover for top 3 lines of file
                if lineindex<3:
                    if i<3:
                        count+=getDownRight(lines, lineindex, i)
                    elif i>=len(line)-3:
                        count+=getDownLeft(lines, lineindex, i)
                    else:
                        count+=getDownLeft(lines, lineindex, i)
                        count+=getDownRight(lines, lineindex, i)
                #cover for last 4 lines of file
                elif lineindex>=len(lines)-3:
                    if i<3:
                        count+=getUpRight(lines, lineindex, i)
                    elif i>=len(line)-3:
                        count+=getUpLeft(lines, lineindex, i)
                    else:
                        count+=getUpRight(lines, lineindex, i)
                        count+=getUpLeft(lines, lineindex, i)
                #any middle line of the file
                else:
                    if i<3:
                        count+=getUpRight(lines, lineindex, i)
                        count+=getDownRight(lines, lineindex, i)
                    elif i>=len(line)-3:
                        count+=getUpLeft(lines, lineindex, i)
                        count+=getDownLeft(lines, lineindex, i)
                    else:
                        count+=getUpLeft(lines, lineindex, i)
                        count+=getUpRight(lines, lineindex, i)
                        count+=getDownLeft(lines, lineindex, i)
                        count+=getDownRight(lines, lineindex, i)
    return count




def getDown(lines, lineindex, ind):
    if((lines[lineindex+1][ind]=="M") and (lines[lineindex+2][ind]=="A") and (lines[lineindex+3][ind]=="S")):
        return 1
    else:
        return 0
    
def getDownRight(lines, lineindex, ind):
    if((lines[lineindex+1][ind+1]=="M") and (lines[lineindex+2][ind+2]=="A") and (lines[lineindex+3][ind+3]=="S")):
        return 1
    else:
        return 0
def getDownLeft(lines, lineindex, ind):
    if((lines[lineindex+1][ind-1]=="M") and (lines[lineindex+2][ind-2]=="A") and (lines[lineindex+3][ind-3]=="S")):
        return 1
    else:
        return 0
    
def getUp(lines, lineindex, ind):
    if((lines[lineindex-1][ind]=="M") and (lines[lineindex-2][ind]=="A") and (lines[lineindex-3][ind]=="S")):
        return 1
    else:
        return 0

def getUpRight(lines, lineindex, ind):
    if((lines[lineindex-1][ind+1]=="M") and (lines[lineindex-2][ind+2]=="A") and (lines[lineindex-3][ind+3]=="S")):
        return 1
    else:
        return 0
    
def getUpLeft(lines, lineindex, ind):
    if((lines[lineindex-1][ind-1]=="M") and (lines[lineindex-2][ind-2]=="A") and (lines[lineindex-3][ind-3]=="S")):
        return 1
    else:
        return 0

def main():
    test='WordsearchTest.txt'
    file='Wordsearch.txt'
    lines=accessfile(file)
    countXMAS(lines)

main()

"""if (lineindex>2 and lineindex<len(lines)-3) and (i>2 and i<len(line)-3):
                    count+=getUp(lines, lineindex, i)
                    count+=getUpRight(lines, lineindex, i)
                    count+=getUpLeft(lines, lineindex, i)
                    count+=getDown(lines, lineindex, i)
                    count+=getDownLeft(lines, lineindex, i)
                    count+=getDownRight(lines, lineindex, i)
                else:
                    if lineindex<=2:
                        count+=getDown(lines, lineindex, i)
                        if i>2 and i<len(line)-3:
                            count+=getDownRight(lines, lineindex,i)
                            count+=getDownLeft(lines, lineindex, i)
                        else:
                            if i<2:
                                count+=getDownRight(lines, lineindex,i)
                            else:
                                count+=getDownLeft(lines, lineindex, i)
                    if lineindex > (len(lines)-3):
                        count+=getUp(lines, lineindex, i)
                        if i>2 and i<len(line)-3:
                            count+=getUpRight(lines, lineindex,i)
                            count+=getUpLeft(lines, lineindex, i)
                        else:
                            if i<2:
                                count+=getUpRight(lines, lineindex,i)
                            else:
                                count+=getUpLeft(lines, lineindex, i)"""