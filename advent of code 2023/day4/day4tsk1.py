"""cycle through each of the cards the first match is 1 point. each subsequent match the score is doubled. """

def openfile(filename):
    infile=open(filename,'r')
    line=infile.readline()
    lines=[]
    while line!='':
        numbers=removenum(line[:-1])
        lines.append(numbers)
        line=infile.readline()

    infile.close
    return lines

def removenum(line):
    num=line.split(': ')
    num.remove(num[0])
    return num

def refmy(line):
    #print (line)
    allnum=line[0].split(' | ')
    refnum=allnum[0].split()
    mynum=allnum[1].split()
    #print(mynum, '\n', refnum)
    # count=0
    # for i in range(int(len(refstring)/3)):
    #     #print(i,refnum)
    #     refplace=refstring[i+count]
    #     wholenum=refstring[i+count:i+count+1]
    #     if refplace.isdigit()==True:
    #         refnum.append(wholenum)
    #     else:
    #         refnum.append(refstring[i+count+1])
    #     count+=2   
    # count=0
    # for i in range(int(len(mystring)/3)):
    #     refplace=mystring[i+count]
    #     wholenum=mystring[i+count:i+count+1]
    #     if refplace.isdigit()==True:
    #         mynum.append(wholenum)
    #     else:
    #         mynum.append(mystring[i+count+1])
    #     count+=2
        
    return refnum, mynum

def getnums(cards):
    scores=[]
    for i in cards:
        refnum, mynum=refmy(i)
        score=compare(refnum, mynum)
        if score!=0:
            scores.append(score)

    return scores

def compare(refnum, mynum):
    score=0
    #print(refnum, mynum)
    for i in mynum:
            try:
                locate=refnum.index(i)    
                if score==0:
                    score=1
                else:
                    score=score*2
            except:
               continue
            #print(score)
    return score


def main():
    file='scratchcards.txt'
    #file='sample.txt'
    cards=openfile(file)
    tot=0
    scores=getnums(cards)
    for i in scores:
        tot+=i

    print(tot)


main()
