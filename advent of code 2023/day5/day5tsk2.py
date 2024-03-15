"""the first set of numbers are the seed id numbers now a range referenced by pairs (seed#, number of values in range).
in this task i am to figure out which seed will be in the closest
location. THE LOCATION NUMBER IS MY OUTPUT!
to get this i have to figure out the range for the next level to get the location for each seed within the range.
the catergories are:
seed to soil map
soil to fertilizer
fertilizer to water
water to light
light to temp
temp to humidity
humidity to location
the seed number will fall into a range. "source range". 
the numbers are organized as follows:
destination,  source, range width
basically if the source(output of last section)falls between source and source+rangewidth. its location will then be location+(output-source). 
that will continue down the hill"""

def openread(file):
    infile=open(file,'r')
    line=infile.readline()
    # seeds=line.split(' ')
    # print(seeds)
    # seeds.remove(seeds[0])
    # print(seeds[0])
    body=[] 
    section=''
    counter=7
    while line!='':
        #print('1')
        if line!='\n':
            section=section+line
            #print(section)
        else:
            body.append(section)
            section=''
            counter-=1
        line=infile.readline()
        if line=='':
            body.append(section)                    
        
    #print('2')
    seeds=body[0]
    seeds=seeds[:-1]
    seeds=seeds.split(' ')
    seeds.pop(0)
    seed2soil=makelist(body[1])
    soil2fert=makelist(body[2])
    fert2wat=makelist(body[3])
    wat2lt=makelist(body[4])
    lt2temp=makelist(body[5])
    temp2hum=makelist(body[6])
    hum2loc=makelist(body[7])
           
    
    pipeline=[seed2soil,soil2fert,fert2wat,wat2lt,lt2temp,temp2hum,hum2loc]
    #print(pipeline)
    infile.close
    return seeds, pipeline

def makelist(section):
    #take off title
    notit=section.split(':\n')
    notit.pop(0)
    #sepline=notit[0]
    sepline=notit[0].split('\n')
    #print(sepline[:-1])
    return sepline[:-1]
    
def getloc(seed, pipeline):
    refnum=seed
    #runs the seed through each subsequent list
    for i in pipeline:
        #determines location value in each catergory
        #print(refnum)
        refnum=getval(refnum,i)
    #returns location
    return refnum    

def getval(reference, list):
    #for each line of 3 numbers
    #print(list)
    ref=int(reference)
    #print(list)
    emstop=0
    for i in list:
        line=i.split(' ')
        #print(i, line)
        #source reference location
        sourcestart=int(line[1])
        #print (sourcestart)
        #the end of the range
        sourceend=int(sourcestart+int(line[2])-1)
        #print(sourceend)
        #if it falls within the range        
        if ref>=sourcestart and ref<=sourceend:
            #figures out offset for location placement
            space=ref-sourcestart
            #applies offset
            value=int(int(line[0])+space)
            #returns that value
            return value
    return ref

def smallestrange(seeds, pipeline):
    #Set the place from the end 
    place=-1
    #identifies the full set list of the pipeline starting from the bottom(location)
    set=pipeline[place]
    #sets the number to the largest number in seeds as a jumping off point
    smallestloc=max(seeds)
    #gets the top and bottom of the range of the smallest location
    rngtop, rngbot=reqlow(set,smallestloc)
    #steps up the ladder towards seeds identifying requirements for lowest catergory. 
    for i in range(len(pipeline-1)):
        #moves up pipeline list
        place-=1
        set=pipeline[place]
        rngtop,rngbot=nextrange(set,rngtop, rngbot, )

        
#this function identifies the next range required to fall in the proper previous rung in ladder     
def nextrange(set, rngtop, rngbot):
    print(set)        
            
def reqlow(set, smallestloc):
    for i in set:
        line=i.split(' ')
        line=[int(x) for x in line]
        location=line[0]
        if location<smallestloc:
            smallset=line
        rngbot=smallset[1]
        rngtop=smallset[1]+smallset[3]
    return rngtop, rngbot

def main():
    #file="input.txt"
    file="sample.txt"
    seeds, pipeline =openread(file)
    seeds=[int(x) for x in seeds]
    #print(seeds)
    location=getloc(seeds[0],pipeline)
    counter=0
    possible=smallestrange(seeds, pipeline)
    #checks each seed
    # for i in range (int(len(seeds)/2)):
    #     #print('3')
    #     start=int(seeds[counter])
    #     spread=int(seeds[counter+1])
    #     #print(start, spread)
        
        # if best<location:
        #         location=best

        #counter+=2
    print(location)



main()

#best=doit(location, start, spread, pipeline)
        # for j in range(spread):
        #     #print('3')
        #     active=start+j
        #     print(active)                    
        #     check=getloc(active,pipeline)
        #     #identifies closest plot

#def doit(location,start,spread, pipeline):
#     for j in range(spread):
#             #print('3')
#             active=start+j                    
#             for i in pipeline:
#                  check=getval(active,i)
#             #identifies closest plot
#             if check<location:
#                 location=check