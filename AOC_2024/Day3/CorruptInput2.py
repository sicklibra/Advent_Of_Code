import re
'''Copyright 2024 Robert J. Hodges

this program is the sole production of Robert J Hodges for the Advent of code 2024
Day 2 I accept no responsibility for any damages that may be incurred from the
use and application of this code. For educational use only.

the first problem is to go through the file and anything with mul(#,#) in that order is identified and 
the two ints are multiplied and put into a list. That list is to be added I couldn't get re working properly 
see commented code below. so i took the long route'''
'''Problem 2:
i now need to incorperate the 'do()', and 'don't()' it is like a boolean is flipped, it begins true and then 
is flipped by the do/don't accordingly i will try Regex again now that i may have a chance at putting them into
a search list. I will start with It on and search for r'[do(),don't(), mul]' i will use that index to evaluate
what it is and run the proper while loops in a bool function reading do and if it continues to don't If i absolutely have to i will create a list of the index numbers for each and compare the indexes in a while loop this would be well
suited for an object that stores the value of the multiplied #s and the index for comparison'''
def accessfile(file):
    infile=open(file,'r')
    wholefile=infile.read()
    return wholefile

def findsubstrings(instring):    
    nums=[]
    index=0
    sum=0
    #iterate through whole string by the beginning of the key 'mul('signifying the start of a valid set
    while index>=0:
        num1=""
        num2=""
        #iterates to next valid opening starting from the index left from the last round of while
        index=instring.find("mul(", index, len(instring)-1)
        
        if instring[index+4].isdigit():
            switch=False
            index+=4
            while instring[index].isdigit():
                if switch==False:
                    num1+=instring[index]
                    print(num1)
                    index+=1
                    if instring[index]==',':
                        index+=1
                        if instring[index].isdigit():
                            switch=True
                    else:continue
                else:
                    num2+=instring[index]
                    index+=1
                    print ('n'+ num2)
                    if instring[index]==")":
                        nums.append(int(num1)*int(num2))
                    
    for number in nums:
        sum+=number
    print(sum)
#mul[(]  +[)]

def main():
    file="CorruptInput.txt"
    #file='CorruptTest.txt'
    cfile=accessfile(file)
    print(cfile)
    findsubstrings(cfile)

main()