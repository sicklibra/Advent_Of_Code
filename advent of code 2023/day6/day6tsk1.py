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
    for i in splitted:
        try:
            int(i)
            lst.append(i)
        except:
            continue
    return lst
    
def beatquant(time, dist):
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
            solution+=1
    #print(solution)
    return solution

    



def main():
    file='raceinfo.txt'
    #file='test.txt'
    time, distance=getinfo(file)
    #change lists to integers.
    time=[int(x) for x in time ]
    distance=[int(x) for x in distance]
    #empty lists and variable initializations.
    solutions=[]
    position=0
    ans=1
    #determines the number of possible outcomes for each time/distance bracket
    for i in time:
        #syncs up the distance variable with the time variable
        dist=distance[position]
        #finds number of possible solutions
        num=beatquant(i,dist)
        #appends possible solutions to list to be calculated(could consolidate in this list but wanted to see every step for trouble shooting.)
        solutions.append(num)
        #changes position of the distance list to match time slot.
        position+=1
    for i in solutions:
        ans*=i
    print(ans)
main()