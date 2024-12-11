'''Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only

this one is gonna be fun! in the text file there is a ^ this marks the position of the guard. the guard starts in the direction of the ^ so i will use ^,v,<,> for directions when the guard comes adjacent to a # it will turn 90deg to the right, repeating this movement until it exits the map. the goal is to count how many unique positions the guard visits prior to leaving the map. 
I feel the matrix style is a good fit for this a list of lists accounting for each line if ^ list[y-1][x](this will work like an inverted graph) if > list[y][x+1] if <list[y][x-1] and v list[y+1][x] this will continue turning each point into an x until one of the indexes is out of bounds.'''


def mapFile(file):
    infile=open(file,'r')
    line=infile.readline()
    map=[]
    while line!='':
        lnlst=line[:-1]
        mapline=list(lnlst)
        map.append(mapline)
        line=infile.readline()
    return map

def getPositions(map):
    y,x=findGuard(map)
    mapPath(map, y, x)
    for line in map:
        # print(line)
    count=0
    for row in map:
        for point in row:
            if point=="x":
                count+=1
    print (count)

def findGuard(map): 
    # print(len(map), len(map[0]))
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x]== "^":
                return y,x
            # else:
            #     return 0,0

def mapPath(map, y, x):
    while y<len(map) and y>=0 and x>=0 and x<len(map[0]):
        # for i in map:
        #     print(i)
        if map[y][x]=="^":
            if map[y-1][x]=="#":
                map[y][x]=">"
            else:
                map[y][x]='x'            
                y-=1
                map[y][x]='^'
        elif map[y][x]=='>':
            if map[y][x+1]=='#':
                map[y][x]='v'
            else:
                map[y][x]='x'
                x+=1
                map[y][x]=">"
        elif map[y][x]=='v':
            if map[y+1][x]=='#':
                map[y][x]="<"
            else:
                map[y][x]='x'
                y+=1
                map[y][x]='v'
        elif map[y][x]=='<':
            if map[y][x-1]=='#':
                map[y][x]='^'
            else:
                map[y][x]='x'
                x-=1
                map[y][x]='<'


def main():
    file='Map.txt'
    test='test.txt'
    map=mapFile(file)
    # print(map)
    getPositions(map)
    

main()