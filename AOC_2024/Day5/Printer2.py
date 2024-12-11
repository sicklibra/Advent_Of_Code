'''The text file provided has a set of rules in the format int|int and a series of numbers following the format:
 int,int,int... each number in the list must adhere to the rules above ie if rule is 45|61, 61 must come after 41 in the list. if the list is valid the center number is to be added to the solution pool giving a single number input
 my approach:
 1) Read the file put a counter in the read to mark the spot as my sentinal for the while loop counting the empty
    lines terminating when it gets to the second empty line
2)if the length of the line is less than 6 meaning it follows the format ##|## which all rules are 2 digits it
    will be appended to the rule list as a tuple by splitting on the | and doing a quick for loop for each to 
    turn them into ints for comparison and sort the tuples for faster accessing(a hash table would work better
    but i admittedly dont know how to use one)
3)The rest of the file will go into a list of lists of values
        using a for loop turn all values into ints
4) for each item in the list of values, compare to all previous values by referencing the rules by the 
    previous number being compared to make sure they fall in correct order
        caviat: if the number doesnt have an explicit rule it can be wherever
5) if the comparisons are completed successfully, find middle number by referencing the index
    line(len//2) and add that to the sum pool'''

'''problem2:
uses only the lists that fail the rule test. The sum is come to by the same way, in that once it passes the test, it will
add the center integers. the way i will accomplish this is to create a dummy list and check it against the matrix using my 
old function. it will work the same way, but if it hits a failure, it will take the number and compare it to all of the other
numbers in the list. when it finds a suitable spot, it is inserted it will then run a check again to make sure all are in place. '''



def accessFile(file):
    infile=open(file,'r')    
    rules=[]
    input=[]
    counter=0
    while counter<2:
        line=infile.readline().rstrip()        
        if line=="":
            counter+=1
        elif len(line)<6:
            rulestr=line.split("|")
            rule=list(map(int, rulestr))
            # print(rule)
            rules.append(rule)
        else:
            numstr=line.split(",")
            nums=list(map(int, numstr))
            input.append(nums)
    rules.sort()
    return rules, input

def getCount(rules, input):
    sum=0
    for set in input:
        # print(set)
        if compare(rules, set)==False:
            sum+=makeRight(rules, set)
        
    print(sum)

def makeRight(rules, set):
    for i in range(len(set)):
        ival=set[i]
        j=i+1
        while j<len(set)-1:
            jval=set[j]
            if rules[jval][ival]:
                #inserts i after J
                findspot(rules, set, i, j)
                if compare(rules,set)==True:
                    return set[len(set)//2]
                else:
                    j+=1
            else:
                j+=1
        j=i-1
        while j>=0:
            jval=set[j]
            if rules[ival][jval]==1:
                findspot(rules, set, i, j)
                if compare(rules, set)==True:
                    return set[len(set)//2]
                else:
                    j-=1
            else:
                j-=1
    print("something didn't go as planned")    

def findspot(rules, set, i, j):
    temp=set[i]
    potpos=0
    for num in set:
        if i<j:
            
        if potpos==i:
            continue
        elif rules[potpos][temp]==1:
            continue


def insertAfter(set, i, j):
    temp=set[i]
    while i<j:
       set[i]=set[i+1]
       i+=1
    set[j]=temp

def insertBefore(set, i, j):
    temp=set[i]
    while j<i:
        set[i]=set[i-1]
        i-=1
    set[j]=temp

def compare(rules, set):
    for i in range(len(set)):
        #reference the inverse of each of the items to matrix. if there is a 1 in that position,
        #it fails because a rule has been violated
        ival=set[i]
        j=i+1
        while j<len(set)-1:
            jval=set[j]
            if rules[jval][ival]==1:
                return False
            else:
                j+=1
        j=i-1
        while j>=0:
            jval=set[j]
            if rules[ival][jval]==1:
                return False
            else:
                j-=1

    return True

#because all values are 2 digits a 100x100matrix will suffice
def toMatrix(rulelst):
    matrix=[]    
    for i in range(100):
        secval=[]
        for i in range(100):
            secval.append(0)        
        matrix.append(secval)
    for set in rulelst:
        val1=set[0]
        val2=set[1]
        matrix[val1][val2]=1
    return matrix
        

def main():
    file='Printercode.txt'
    test='PrinterTest.txt'
    rules, input= accessFile(file)
    rules=toMatrix(rules)
    # print (rules)
    # print (input)
    getCount(rules, input)



main()