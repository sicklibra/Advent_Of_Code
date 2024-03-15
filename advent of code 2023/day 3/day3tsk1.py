def readfile(filename):
    infile=open(filename,'r')
    body=infile.read()    
    infile.close()
    return body

# def locate(lst):
#     line1=lst[0]
#     line2=lst[1]
#     line3=lst[2]    
#     space, count=itlen(line1)
    
#     while space>0:        
#         numid=0
#         for i in range (len(line1)-count):
#             try:
#                 num=line1[i+numid]
#                 space-=2
#                 numid+=2
#             except:
#                  space-=1


def locateln1 (numlst,line1, line2):
    #space, count=itlen(line1)
    space=len(line1)        
    numid=0
        #print('numid=',numid)
    for i in range (space):
      try:      
        if line1[i+numid].isdigit()==True:
            numlen=0                
            for f in range(5):
                if line1[f+i+numid].isdigit()==True:
                    numlen+=1
                    # print(line1[f+i+numid])
                else:
                    break
                                         
            part=searcharound(line2,i+numid,numlen)
            if part==True:
                 numlst.append(str(line1[i+numid:i+numid+numlen]))
                 #print('i+numid=',i+numid,numlst)
                 #numid+=numlen
            elif line1[i+numid-1]!='.' or line1[i+numid+4]!='.': 
                numlst.append(str(line2[i+numid:i+numid+numlen]))
                #numid+=numlen
            #print('numlen=',numlen,'numid=',numid)
            numid+=numlen-1
        # else:
        #     space-=1
      except:
          break          
    return numlst


def locaterest(numlst,line1,line2, line3):
    #space,count=itlen(line2)
    space=len(line2)
    #print(line2)
    #print(space,count)
    numid=0
    for i in range (space):
      try:      #print('numid=',numid)
        if line2[i+numid].isdigit()==True:
            numlen=0                
            for f in range(5):
                if line2[f+i+numid].isdigit()==True:
                    numlen+=1
                else:
                    break  
            #number=str(line2[i+numid:i+numid+numlen])
            #print (number)          
            parttop=searcharound(line1,i+numid,numlen)
            partbottom=searcharound(line3,i+numid,numlen)
            if parttop==True or partbottom==True:
                numlst.append(str(line2[i+numid:i+numid+numlen]))
                # numid+=numlen
            # elif line2[i+numid-1]!='.' or line2[i+numid+numlen+1]!='.': 
            #     numlst.append(str(line2[i+numid:i+numid+numlen]))
            elif line2[i+numid-1]!='.': 
                numlst.append(str(line2[i+numid:i+numid+numlen]))
            try:
                endline=line2[i+numid+numlen]
                if endline!='.':
                    numlst.append(str(line2[i+numid:i+numid+numlen])) 
            except:continue                
            numid+=numlen-1
            #print("numlen=",numlen,'numid=',numid,end=',')
      except:break  
    return numlst 

def lastline(numlst, refline, lstline):
    #print(refline,'/n',lstline)
    #space,count=itlen(lstline)  
    space=len(lstline)      
    numid=0
    #print(space)
    for i in range (space):
      try:  #print(numid+i)
        if lstline[i+numid].isdigit()==True:
            numlen=0 
                           
            for f in range(5):
                if lstline[f+i+numid].isdigit()==True:
                    numlen+=1
                else:
                    break
                               
            part=searcharound(refline,i+numid,numlen)
                #print (part0
            if part==True:
                numlst.append(str(lstline[i+numid:i+numid+3]))
                    #numid+=numlen
            elif lstline[i+numid-1]!='.': 
                numlst.append(str(lstline[i+numid:i+numid+3]))
                    #numid+=numlen 
            try:
                endline=lstline[i+numid+numlen]
                if endline!='.':
                    numlst.append(str(lstline[i+numid:i+numid+numlen])) 
            except:continue                                 
            numid+=numlen-1
      except:
          break  
    return numlst
     
def searcharound(line, position,numlen):
    position-=1
    #print("position=",position)
    for i in range(numlen+2):
         if line[position+i]!='.' and line[position+i].isdigit()==False:
              return True
         elif position+i>len(line):
              break
    return False 
              
     
def itlen(line):
    count=0
    numbers=0
    counter=0
    for i in line:
        if i.isdigit()==True:
            count+=1
            for f in range (5):
                if line[counter+f+1].isdigit:
                    numbers+=1
                else:
                    break
        counter+=1
    #print('count=',count)
    count-=numbers
    space=len(line)-count
    return space, count
     

def main():
    file='enginecode.txt'
    #file="test.txt"
    body=readfile(file)
    lst=body.split("\n")
    numlst=[]
    numlst=locateln1(numlst,lst[0],lst[1])
    #print(numlst)
    #starts with previous "line2 "
    linecounter=0
    while lst[linecounter+2]!='':
        numlst=locaterest(numlst, lst[linecounter],lst[linecounter+1],lst[linecounter+2])
        linecounter+=1
    numlst=lastline(numlst,lst[-3],lst[-2])
    print(numlst)
    tot=0
    for i in numlst:
        #print(i, end=',')
        tot+=int(i)
    print(tot)


main()