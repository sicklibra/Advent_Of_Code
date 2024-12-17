"""The input for this puzzle is a series of dots and characters. The characters are symbolic of an antenna transmitting on a 
different wavelength. The antenodes are at positions that correspond between two broadcasts of the same frequency. the correlation is 
that the antenode is a distance from one  and twice that distance from the next. These correlations are made in any direction
so .aa. will have an antenode at each of the periods because one is one pos away and the other is two. if it falls outside of
the bounds of the matrix, it is invalid.
problem 1: count up the number of unique antinode positions overlaps between different antennas still only count as 1 
Process:
1 make a matrix of the inputs
2 scan matrix and compile a list of the characters. cull that list so that each character appears once
3 for each unique character, compile a list of the positions of each antenode. 
4 compare thoses lists to eachother to get list of unique positions.
get the length of that list"""
import math

#turn the text file into a useable matrix.
def makeMatrix(file):
    infile=open(file,'r')
    matrix=[]
    line=infile.readline().rstrip()
    while line!="":
        linesep=list(map(str,line))
        matrix.append(linesep)
        line=infile.readline().rstrip()
    return matrix

#get all unique characters
def getChars(matrix):
    chars=[]
    for line in matrix:
        for i in line:
            if i!='.':
                chars.append(i)
    charset=set(chars)
    chars = list(charset)
    return chars

#this gets the list of unique anodes.
def getAnodes(map, chars):
    #create a list of tuples
    antinodes=[]
    """This is where it gets weird. I will use a for loop to iterate through each character in the chars list
    by doing this, i can run independent searches for anodes that will allow for overlapping. by creating a dummy
    matrix for each iteration, i can avoid destroying the original and grab the necessary tuples of the anodes for 
    each character. by then dumping them into a set it will remove all duplicate tuples and leave me with the 
    number of original annode positions. """
    for tower in chars:
        charstuples=findTuples(map, tower)
        for tup in charstuples:
            antinodes.append(tup)
    antinodeset=set(antinodes)
    antinodes=list(antinodeset)
    print(len(antinodes))

def findTuples(map, tower):
    i=0
    height=len(map)-1
    width=len(map[0])-1
    tuplst=[]    
    while i<=height:
        j=0
        while j<= width:
            if map[i][j]==tower:
                mark1=(i,j)
                anodes=allFromMark(map, mark1, height, width, tower)
                for tups in anodes:
                    tuplst.append(tups)
                j+=1
            else:
                j+=1
        i+=1
    return tuplst

def allFromMark(map, mark1, height, width, tower):
    anodes=[]
    i=mark1[0]+1
    while i<=height:
        j=0
        while j<= width:
            if map[i][j]==tower:
                mark2=(i,j)
                nodes=getem(mark1, mark2, height, width)
                for tups in nodes:
                    anodes.append(tups)
                j+=1
            else:
                j+=1
        i+=1
    return anodes        

def getem(mark1, mark2, height, width):
    anodes=[]
    vert=mark2[0]-mark1[0]
    horiz=abs(mark1[1]-mark2[1])
    ytop=mark1[0]-vert
    ybot=mark2[0]+vert
    if mark1[1]<mark2[1]:        
        xtop=mark1[1]-horiz        
        xbot=mark2[1]+horiz
        if ytop>=0 and xtop>=0:
            node=(ytop,xtop)
            anodes.append(node)
        if ybot<=height and xbot<=width:
            node=(ybot, xbot)
            anodes.append(node)
    else:
        xtop=mark1[1]+horiz
        xbot=mark2[1]-horiz
        if ytop>=0 and xtop<=width:
            node=(ytop,xtop)
            anodes.append(node)
        if ybot<=height and xbot>=0:
            node=(ybot, xbot)
            anodes.append(node)
    return anodes
    
    

def main():
    file="Antennas.txt"
    test="test.txt"
    matrix=makeMatrix(file)
    characters=getChars(matrix)
    getAnodes(matrix, characters)

main()