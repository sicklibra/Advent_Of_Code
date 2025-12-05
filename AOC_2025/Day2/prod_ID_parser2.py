'''the input is given as a single line with ranges separated by commas.
the range high and low are separated by a hyphen. 
I am to find any value in the range that is made up of a repeating pattern. so, the idea is
to take the file read it into a line split on comma then with each list item split on hyphen. 
that will give me a high and low in each element. It will be a little computationally heavy, 
but i will basically count through each element of the list and compare the first half to the 
second half of the number. In the second part i need to check if there are multiple repeats. so I willl
need to subdivide the numbers but the whole number must be a repeating sequence. '''

def readFile(file):
    infile=open(file,'r')
    line=infile.readline()
    line.replace('\n','')
    lnlst=line.split(',')
    outlst=[]
    # print (lnlst)
    for i in lnlst:
        item=i.split('-')
        for j in item:
            j=int(j)
        # print(item)
        outlst.append(item)
    # print (outlst)
    return outlst

def getSum(ranges):
    runningtot=0
    for rng in ranges:
        low=int(rng[0])
        high=int(rng[1])
        for i in range((high+1)-low):
            num=low+i
            runningtot+=checknum(num)

    print(runningtot)

'''This is gonna get weird. to find the mid point of a number i am going to have to convert the
number to a string, get the length, get the substring, and compare.'''
def checknum(num):
    num=str(num)
    if len(num)==1:
        return 0
    half=int(len(num)/2)
    if len(num)%2==1:
        return multiCheck(num, half)
    else:
        num1=int(num[0:half])
        num2=int(num[half:])
        if num1==num2:
            # print(num)
            return int(num)
        else:
            return multiCheck(num, half)
        
def multiCheck(num, half):
    repchk=int(num[0])
    same=True
    for i in range(len(num)):
        if int(num[i]) != repchk:
            same=False
            break
    if same==True:
        print(num)
        return int(num)
    for i in range(2, half):
        if len(num) % i == 0:
            chunk=int(num[0:i])
            same=True
            for j in range(len(num) // i):
                start=i*j
                end=(i*j)+i
                chunks=int(num[start:end])
                if chunks!= chunk:
                    same=False
            if same==True:
                print (int(num))
                return int(num)
    return 0

def main():
    # ranges=readFile('test.txt')
    ranges=readFile('day2_input.txt')
    getSum(ranges)

main()
