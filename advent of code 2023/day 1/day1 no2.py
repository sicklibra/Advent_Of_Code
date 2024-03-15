def getnumbers(filename):
    infile=open(filename,'r')
    line=infile.readline()
    numbers=[]
    
   
    while line!='':
        print (line)
        #list that gets rebuilt to consolidate
        tempnum=[]
        for i in line:
            tempnum.append('x')
        #find ints
        #print(tempnum)
        tempnum=intsort(tempnum, line)
        #print(tempnum)
        #find txt numbers
        tempnum=txtsort(tempnum, line)
        tempnum2=[]

        for i in tempnum:
            if i!="x":
                tempnum2.append(i)
        print(tempnum, tempnum2)

        #print(tempnum)
        if len(tempnum2)==1:
            value=int(str(tempnum2[0])+str(tempnum2[0]))
        elif len(tempnum2)>=3:
            value=int(str(tempnum2[0])+str(tempnum2[-1]))
        else:
            value=int(str(tempnum2[0])+str(tempnum2[1]))
        numbers.append(value)
        line=infile.readline()
    print(numbers)
    return numbers
            
def intsort(tempnum,line):
    txtnum=["0",'1','2','3','4','5','6','7','8','9']
    for i in txtnum:
            pos=line.find(i)
            it=1
            dup=-1
            while pos!=-1:
                    if dup!=pos:
                        tempnum[pos]=txtnum.index(i)
                    elif pos==dup:
                         pos=-1
                    it+=1
                    dup=pos
                    pos=line.find(i,it)
    return tempnum

def txtsort(tempnum,line):
     txtnum=["zero",'one','two','three','four','five','six','seven','eight','nine']
     for i in txtnum:
            pos=line.find(i)
            it=0
            dup=-1
            while pos!=-1:
                    if dup!=pos:
                        tempnum[pos]=txtnum.index(i)
                    elif pos==dup:
                         pos=-1
                    it+=1
                    dup=pos
                    pos=line.find(i,it)
                   
                    
                    
                    #print(tempnum,pos)
     return tempnum

def main():
    file="scramble.txt"
    #file="testlines.txt"
    numbers=getnumbers(file)
    tot=0
    #print(numbers)
    for i in numbers:
        tot+=i

    print(tot)





main()