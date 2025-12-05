'''The lines in the input text are the battery banks with the 'joltage' being the numeric value of the battery
each number= 1 battery, the goal is to find the sum of the maximum joltage of each line. as stated in the example
a line consisting of 12345, batteries 2 and 4 would equal 24 jolts. so the max for this line would be 45 jolts

I will accomplish this by reading each line into a string. I will then compare each item in the string. 
if a 9 is found. that will immediately be marked as the first battery. Then i will find the next highest 
battery. so i will mark the index and the number and then concat the strings and change to an int to be added.'''

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
    max1=0
    max2=0
    #this loop will not check the last element in the line.
    for i in range(len(instr)-1):
        num1=int(instr[i])
        if num1==9:
            ind1=i
            max1=num1
            break
        else:
            if num1 > max1:
                max1=num1
                ind1=i
    for i in range(ind1+1, len(instr)):
        num2=int(instr[i])
        if num2>max2:
            max2=num2
            ind2=i
    return int(instr[ind1]+instr[ind2])


def main():
    # lns=readFile('test.txt')
    lns=readFile('day3_input.txt')
    getTot(lns)


main()