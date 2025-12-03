'''the input is given as a single line with ranges separated by commas.
the range high and low are separated by a hyphen. 
I am to find any value in the range that is made up of a repeating pattern. so, the idea is
to take the file read it into a line split on comma then with each list item split on hyphen. 
that will give me a high and low in each element. It will be a little computationally heavy, 
but i will basically count through each element of the list and compare the first half to the 
second half of the number. '''

def readFile(file):
    infile=open(file,'r')
    line=infile.readline()
    line.replace('\n','')
    lnlst=line.split(',')
    outlst=[]
    print (lnlst)
    for i in lnlst:
        item=i.split('-')
        for j in item:
            j=int(j)
        print(item)
        outlst.append(item)
    print (outlst)
    return outlst

def getSum(ranges):
    runningtot=0
    for rng in ranges:
        low=int(rng[0])
        high=int(rng[1])
        for i in range((high+1)-low):
            runningtot+=checknum(low+i)

    print(runningtot)

'''This is gonna get weird. to find the mid point of a number i am going to have to convert the
number to a string, get the length, get the substring, and compare.'''
def checknum(num):
    num=str(num)
    half=int(len(num)/2)
    if len(num)%2==1:
        return 0
    else:
        num1=int(num[0:half])
        num2=int(num[half:])
        if num1==num2:
            # print(num)
            return int(num)
        else:
            return 0

def main():
    # ranges=readFile('test.txt')
    ranges=readFile('day2_input.txt')
    getSum(ranges)

main()
