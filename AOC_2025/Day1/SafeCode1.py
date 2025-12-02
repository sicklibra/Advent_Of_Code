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
        lnlst.append(line.trim())
        line=infile.readline()
    return lnlst

''' The way to handle this one is to take the numbers and add or subtract in accordance with left and right
left will be addition and right will be subtraction. Take the final number and take the abs value of that number and 
if it is over 1000 mod 1000 then mod 100 and that will give me the 0-99 value that I am looking for
then if it is 0 add it to the count.'''
def main():
    lns = readFile('day1_input.txt')
