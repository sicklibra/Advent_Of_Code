def getinfo(file):
    infile=open(file,'r')

    line=infile.readline()   
    time=listgen(line)
    line=infile.readline()
    dist=listgen(line)

    infile.close()

    return time, dist
    

def listgen(line):
    splitted=line.split()
    lst=[]
    num=''
    for i in splitted:
        try:
            int(i)
            lst.append(i)
        except:
            continue
    for i in lst:
        num+=str(i)
    num=int(num)
    return num
    
def lowbeat(time, dist):
    #print (time, dist)
    solution=0
    for i in range (time):
        #i indicates the speed
        #the amount of time the boat will travel
        gotime=(time-i)
        #amount of distance that can be traveled at the determined speed in the amount of time left.
        distance=i*gotime 
        #identifies if it will go beyond the record mark.       
        if distance>dist:
            return i

def highbeat(time, dist):
    for i in range(time):
        holdtime=time-i
        distance=i*holdtime
        if distance>dist:
            return holdtime

    



def main():
    file='raceinfo.txt'
    #file='test.txt'
    time, distance=getinfo(file)
    print(time, distance)
    low=lowbeat(time, distance)
    high=highbeat(time, distance)
    quant=time-low-(time-high)
    print(quant+1)
    
    
    #print(ans)
main()