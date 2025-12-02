# import math

def accessfile(file):
    infile=open(file,'r')
    line=infile.readline()
    lnlst=[]
    while line!='':
        lnlst.append(line[:-1])
        line=infile.readline()
    return lnlst

def sepNSort(numlst):
    left=[]
    right=[]
    for set in numlst:
        rl=set.split("   ")
        left.append(int(rl[0]))
        right.append(int(rl[1]))
    
    left.sort()
    right.sort()
    return left, right

def crossMultiply(left, right):
    j=0
    i=0
    sum=0
    """as we iterate through the left list, we must first find if there is a match on the right list
    if the right side gets larger than or equal to the left value it will continue to iterate. that is why j is
    declared out of the loop once a match is found between the left and right lists, it will move to
    the number of matches the equation once the number of matches has been found on each side will be:
    (number of times left list matches) * ((left number)* (number of times repeated on the right))"""
    while i<=len(left)-1:
        while  j<= len(right)-1 and right[j] < left[i]:
            j+=1
        if j>len(right)-1:
            j=len(right)-1
            
        if left[i]== right[j]:
            key=left[i]
            #the returns will iterate to the end of the matched run
            xRepeatL, i = numMatches(left, i)
            xRepeatR, j = numMatches(right, j)
            sum+=(xRepeatL)*(key*xRepeatR)
        else:
            i+=1
    print(sum)
    


def numMatches(refl, ind):
    repeats=0
    key=refl[ind]
    while ind <= (len(refl)-1) and refl[ind] == key: 
        repeats+=1
        ind+=1
    return repeats, ind


def main():
    # file = 'distancesTest.txt'
    file = "./Distances.txt"
    allnums=accessfile(file)
    left, right=sepNSort(allnums)
    sum=0
    crossMultiply(left, right)
    # for i in range(len(left)):
    #     sum+= abs(int(left[i])-int(right[i]))
    # print(sum)


main()
