"""the first set of numbers are the seed id numbers.
in this task i am to figure out which seed will be in the closest
location. THE LOCATION NUMBER IS MY OUTPUT!
to get this i have to figure out the range for the next level to get the location.
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
        #print(line)
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
        
    #print(body)
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
        #print(refnum,)
        refnum=getval(refnum,i)
    #returns location
    return refnum    

def getval(reference, list):
    #for each line of 3 numbers
    ref=int(reference)
    #print(list)
    for i in list:
        line=i.split(' ')
        #print(line)
        #source reference location
        sourcestart=int(line[1])
        #the end of the range
        sourceend=int(sourcestart+int(line[2])-1)
        #if it falls within the range
        if ref>=sourcestart and ref<=sourceend:
            #figures out offset for location placement
            space=ref-sourcestart
            #applies offset
            value=int(int(line[0])+space)
            #returns that value
            return value
    return ref
def main():
    file="input.txt"
    #file="sample.txt"
    seeds, pipeline =openread(file)
    location=getloc(seeds[0],pipeline)
    #checks each seed
    for i in seeds:
        check=getloc(i,pipeline)
        #identifies closest plot
        if check<location:
            location=check
    print(location)



main()