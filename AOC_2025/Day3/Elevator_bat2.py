'''The lines in the input text are the battery banks with the 'joltage' being the numeric value of the battery
each number= 1 battery, the goal is to find the sum of the maximum joltage of each line. as stated in the example
a line consisting of 12345, batteries 2 and 4 would equal 24 jolts. so the max for this line would be 45 jolts
3.2:
Now the joltage has to be a combination of 12 batteries I will have to look at the first set of numbers leading up
to there being a minimum of 12 digits left. I will then start looking from the tail end to find the largest value leaving
up to 10 unaccounted for items in the end. the max should be an amalgamation of the  internal numbers'''

def readFile(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line.strip('\n'))
        line=infile.readline()
    # print(lnlst)
    return lnlst

def getTot(lst):
    runTot=0
    for i in lst:
        runTot+=batVal(i)
    print(runTot)

def batVal(instr):
    ind1=0
    ind2=0
    indexes=[]
    max1=0
    max2=0
    outstr=""
    #this loop will not check the last element in the line.
    #this will get me my starting index to work with
    for i in range(len(instr)-11):
        num1=int(instr[i])
        if num1==9:
            ind1=i
            max1=num1
            break
        else:
            if num1 > max1:
                max1=num1
                ind1=i
    indexes.append(ind1)
    #this will determine my end value point starting from the end of the line
    for i in range(len(instr)-ind1-11):
        num2=int(instr[(len(instr)-1)-i])
        if num2>max2:
            max2=num2
            ind2=i

    #now to work with the substring
    wrkingstr= instr[ind1+1:ind2]
    wrkarr=wrkingstr.split('')
    if len(wrkarr)==12:
        for i in wrkarr:
            indexes.append(i)
        for i in indexes:
            outstr+=i
        outstr+=instr[ind2]
    else:
        mid=getMiddle(wrkingstr, 2)

    return int(outstr)

def getMiddle(arr, pos):
    if len(arr)==12:
        return arr
    for i in 

def main():
    # lns=readFile('test.txt')
    lns=readFile('day3_input.txt')
    getTot(lns)


main()