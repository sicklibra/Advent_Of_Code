def getnumbers(filename):
    infile=open(filename,'r')
    line=infile.readline()
    numbers=[]
    print (line)
    while line!='':
        tempnum=[]
        for i in line:
            try:
                int(i)
                num=i
            except:
                continue
            tempnum.append(num)
        if len(tempnum)==1:
            value=int(str(tempnum[0])+str(tempnum[0]))
        elif len(tempnum)>=3:
            value=int(str(tempnum[0])+str(tempnum[-1]))
        else:
            value=int(str(tempnum[0])+str(tempnum[1]))
        numbers.append(value)
        line=infile.readline()

    return numbers
            


def main():
    file="scramble.txt"
    numbers=getnumbers(file)
    tot=0
    print(numbers)
    for i in numbers:
        tot+=i

    print(tot)





main()