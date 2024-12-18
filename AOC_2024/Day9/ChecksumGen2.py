"""
Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only.

This problem takes a string of text that is exceedingly long. the values of that text alternate in meaning the
first number is the number of occupied file locations the second is the number of free spaces. to decompress this list
i must open everything up the file number is that of the index of its order of insertion. so 2342 would break out
to: 00...1111.. and so on down the line. once the list is generated, i must go from the end of the list and move the
item from the end into the first available empty space. 
once the list has been compressed down to no empty space, the checksum is found by finding the sum of all of the 
products of the value multiplied by it's index. 

problem 2: for this one i will be moving blocks instead of individual files leaving small gaps. so starting from 
the end, the first gap that is available that can fit the whole block will now take the whole block if a set is 
skipped because there is no block big enough to fit it, it remains where it is. the sum is calculated the same way but will 
be a larger number.
"""
def getlist(file):
    infile=open(file,'r')
    line=infile.readline().rstrip()
    intlst=list(map(int, line))
    # print(intlst)
    return intlst

def decompress(complst):
    decomplst=[]
    indcounter=0
    for i in range(len(complst)):
        numiterations=complst[i]
        if i%2==0:
            for j in range(numiterations):
                decomplst.append(indcounter)
            indcounter+=1
        else:
            for j in range(numiterations):
                decomplst.append(".")
    # print(decomplst)
    return decomplst

"""utilizing an i (front of list) and j(end of list) this funct will iterate forward  until i>j then list will be 
condensed. when a '.' is found in i, it will begin checking j until j != '.' i will be replaced with val j and j will be 
replaced with '.' """       
def condense(decomplst):
    j=len(decomplst)-1
    while True:
        jblock=0
        if decomplst[j]!='.':
            i=0
            item=decomplst[j]
            while decomplst[j]==item:
                jblock+=1
                j-=1
            while i<j:
                if decomplst[i]=='.':
                    k=i
                    kblock=0
                    while decomplst[k]=='.':
                        kblock+=1
                        k+=1
                    if kblock>=jblock:
                        for place in range(jblock)


def getsum(lst):
    i=0
    sum=0
    while lst[i]!='.':
        sum+=lst[i]*i
        i+=1
    return sum

def main():
    file='input.txt'
    test='test.txt'
    numlst=getlist(file)
    decomp=decompress(numlst)
    condensed=condense(decomp)
    checksum=getsum(condensed)
    print(checksum)


main()