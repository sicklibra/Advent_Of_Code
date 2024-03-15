"""hands and bids are input from text file includingn 5 cards and a bid separated by a spce. 
hands are ranked as follows:
1 high card
2 pair
3 two pair
4 3 of a kind
5 full house "xxyyy"
6 4 of a kind
7 5 of a kind
if two hands are equal score they are ranked within the bracket by the highest card at the beginning, if equal it moves to the next card and so on. the ranks of the cards in decending order are A K Q J T 9 8 7 6 5 4 3 2 1.
the goal is to output a single number which is the sum of the products of the bids* thier rank in the total heirarchy. 

Process:
Get all of the hands and bids input
determine the strength of the hands (rank based on what the hand makes)
order the ranks by high cards in hand. 
mash hands back together to determine overall rank
multiply the bid by the rank
add all of the bid products together"""

#create class for easily handling card and classifying them by rank

cardlist=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
class Hands:
    def __init__(self, cards, bid ):
        self.hand=cards
        self.bid=int(bid)
        # self.score
    #find what type of hand it is based on scoring above. 
    def findScore(self):
        #initialize variables to compare pairs
        check1=0
        check2=0
        #check all of the cards against hand for pairs
        for i in cardlist:
            #count the number of occourances in the hand of the card iterated.
            numappear=self.hand.count(i)
            #if there has been nothing checked or if there is a single occourance, set check1 to the number of that occourance
            if (check1<=1):
                check1=numappear
            #if check 1 already recognizes a pair move to changing check2
            else:
                if (check2<=1):
                    check2=numappear
            
        #with the variables set to the number of occourances in the hand i can set the hand score
        #five of a kind (7)
        if (check2==5 or check1==5):
            return 7
        #four of a kind (6)
        elif(check1==4 or check2==4):
            return 6
        #full house (5)
        elif((check1==2 and check2==3)or(check1==3 and check2==2)):
            return 5
        #Three of a kind (4)
        elif(check1==3 or check2==3):
            return 4
        #two pair (3)
        elif (check1==2 and check2==2):
            return 3
        #pair (2)
        elif (check1==2):
            return 2
        #high card(1)
        else:
            return 1
    #return bid for final funciton   
    def getBid(self):
        return self.bid
    def getHand(self):
        return self.hand
    
def infoToList(file):
    #initialize empty list to send to main
    hblst=[]
    infile=open(file, 'r')
    #read each line of the text file 
    line=infile.readline()
    #print(line)
    #while text still in line continue to read lines
    while (line!=""):
        #append hand and bid to list as individual item
        hblst.append(line[:-1])
        line=infile.readline()
        #print(line)

    infile.close
    #returns list of all of the hands. 
    return hblst

#creates a temporary list to organize for each hand score
def reorder(hands):
    handsort=[]
    if (len(hands)==1):
        handsort.append(hands[0])
        return handsort
    elif (len(hands)==0):
        return handsort
    handsort.append(hands[0])
    if (isLower(hands[1].getHand(),hands[0].getHand())):
        handsort.append(hands[1])
    else:
        handsort.insert(0,hands[1]) 


    for i in handsort:
        print('initial check',i.getHand())  
    for i in hands:
        print(i.getHand(), end=" ")

    for i in hands[2:]:
        testhand=i.getHand()
        indextrack=1
        #print (testhand)
        for f in handsort:
            sortedhand=f.getHand()
            try:
                bothand=handsort[indextrack].getHand()
            except:
                handsort.append(i)
                break
                
            if (indextrack==1 and isHigher(sortedhand,testhand)==False):
                handsort.insert(0, i)
                print('@',sortedhand,testhand)
                # break
                
            elif(isHigher(sortedhand,testhand)==True and isLower(bothand, testhand)==True):
                handsort.insert(indextrack,i)
                #print(len(handsort),"$", sortedhand, testhand, 'lower' )
                break
                
            else:
                indextrack+=1
        # for i in handsort:
        #     print(i.getHand(),end=",") 
        # print("\n \n") 
            
    return handsort
        
        
#compares two hands if and determines if the hand in the list is higer or lower rank than the testhand
def isHigher(handref, handcomp):
    higher=True
    #print('high',handref,handcomp)
    pos=0
    for i in handref:
        #print('higher:',i,handcomp[pos],'\n', cardlist.index(i), cardlist.index(handcomp[pos]) )
        if(cardlist.index(i)<cardlist.index(handcomp[pos])):           
            return True
        elif(cardlist.index(i)>cardlist.index(handcomp[pos])):
            return False
        else: 
            pos+=1

    return False
#compares two hands and determines if the list hand is higher or lower than the test hand. 
def isLower(handref, handcomp):
    lower=True
    #print('low',handref,handcomp)
    pos=0
    for i in handref:
        #print('lower:',i,handcomp[pos],'\n', cardlist.index(i), cardlist.index(handcomp[pos]) )
        if(cardlist.index(i)>cardlist.index(handcomp[pos])):
            #print('lower true',i,handcomp[pos] )
            return True
        elif(cardlist.index(i)<cardlist.index(handcomp[pos])):
            return False
        else: 
            pos+=1

    return False
        
def totalup(hands, rank):

    #initialize sum for current block
    rank+=1
    sum=0
    if (len(hands)==0):
        return sum
    #tally the total of the bids by multiplying bid by overall rank.
    for i in hands:
        
        sum+=i.getBid()*rank
        #rank+=1
    return sum

def lstout(inlst, outlst):
    for i in inlst:
        outlst.append(i)

def main():
    file="camelcard_Hands.txt"
    handlst=infoToList(file)
    #create empy list for objects
    objHnds=[]
    fivekind=[] #7
    fourkind=[] #6
    fullhouse=[] #5
    threekind=[] #4
    twopair=[] #3
    pair=[] #2
    high=[] #1
    #print(handlst)
    for i in handlst:
        item=i.split(" ")
        objHnds.append(Hands(item[0], item[1]))
    # for i in objHnds:
    #         print(i.getHand(), i.getBid(), i.findScore())
    #establish what catergory it falls in and create lists
    for i in objHnds:
        if (i.findScore()==7):
            fivekind.append(i)
        elif(i.findScore()==6):
            fourkind.append(i)
        elif(i.findScore()==5):
            fullhouse.append(i)
        elif(i.findScore()==4):
            threekind.append(i)
        elif(i.findScore()==3):
            twopair.append(i)
        elif(i.findScore()==2):
            pair.append(i)
        else:
            high.append(i)
    
    fivekind=reorder(fivekind) 
    fivekind.reverse()

    fourkind=reorder(fourkind)
    fourkind.reverse()
    
    fullhouse=reorder(fullhouse)
    fullhouse.reverse()
    threekind=reorder(threekind)
    threekind.reverse()
    twopair=reorder(twopair) 
    twopair.reverse()
    pair=reorder(pair)
    pair.reverse()
    high=reorder(high)
    high.reverse()
    #initialize rank tracker and sum
    overallRank=1
    sum=0  
    sumlst=[] 
    lstout(high, sumlst)
    lstout(pair, sumlst)
    lstout(twopair, sumlst)
    lstout(threekind, sumlst)
    lstout(fullhouse, sumlst)
    lstout(fourkind, sumlst)
    lstout(fivekind,sumlst)
    print("sumlst:")
    for i in sumlst:
        print(i.getBid(),"*",overallRank, end=",")
        prod=i.getBid()*overallRank
        sum+=prod
        overallRank+=1
    #figure the sum up for each hand list       
    # sum+=totalup(high, overallRank)
    # overallRank+=len(high)
    # sum+=totalup(pair, overallRank)
    # overallRank+=len(pair)
    # sum+=totalup(twopair,overallRank)
    # overallRank+=len(twopair)
    # sum+=totalup(threekind,overallRank)
    # overallRank+=len(threekind)
    # sum+=totalup(fullhouse,overallRank)
    # overallRank+=len(fullhouse)
    # sum+=totalup(fourkind,overallRank)
    # overallRank+=len(fourkind)
    # sum+= totalup(fivekind, overallRank)
    print('sum',sum)
    
    

if __name__=='__main__':
    main()