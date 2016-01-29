__author__ = 'Andrew.Brown'

def changeDP(coinValueList,value):
    #create table for coinList * value
    minCoins = [[0 for x in range(value+1)]for x in range(len(coinValueList))]
    #fill first line of array with increments of 1
    
    #auxiliary array used to keep track of coins used, will be deconstructed in separate function
    coinsUsed = [[0 for x in range(value+1)]for x in range(len(coinValueList))]
    
     #for first row, we are using pennies, so put increments of 1
    for i in range(value+1):
        minCoins[0][i] = i
       
        coinsUsed[0][i] = i

    #outer loop for coin denomination array
    for i in range(1, len(coinValueList)):
        #inner loop for 0 to value needed+1
        for j in range(value+1):
            #if j is less than the value of the current coin
            #then we still use the count from the previous coin, because current coin is too big
            if j < coinValueList[i]:
                minCoins[i][j] = minCoins[i-1][j]
            #now our current coin is big enough, so we will see if it can get us to the current value of j faster
            #than we did it with the previous coin
            elif j>= coinValueList[i]:
                minCoins[i][j] = min(minCoins[i-1][j], minCoins[i][j-coinValueList[i]]+1)
                coinsUsed[i][j] += 1

    newList = [0]*len(coinValueList) 
    getCoins(len(coinValueList)-1, value, coinValueList, coinsUsed, newList)

    return (minCoins[len(coinValueList)-1][value])

#function to take usedCoins array and break it down to see how many of each coins used
def getCoins(i, j, denom, used, returnThis):
    if j < 0 or i < 0:
        return
 
    if used[i][j] >0:
        returnThis[i] +=1
        #print denom[i]
        #print used[i][j]
        if j-denom[i]<denom[i]:
            #change denomination.
            getCoins(i-1, j-denom[i], denom, used, returnThis)

        else:
            #same denomination
           # print "same denom"
            getCoins(i, j-denom[i], denom, used, returnThis)
            
            
    else:
        print "hi"
        getCoins(i-1, j, denom, used, returnThis)
        

	print returnThis



def changeGreedy(coins,value):
    pocket = []
    sum = 0
    #start with highest value coin (assumes sorted array of denominations)
    for i in range((len(coins)-1), -1, -1):
        temp = value/coins[i]
        pocket += [1,] * temp
        value -= coins[i] * temp
        if temp != 0:
            sum +=1

    return (pocket,sum)



def changeGreedy2(coins, value):
    coinCount = 0
    dictionaryCount = {}
    #start with highest value coin (assumes sorted array of denominations)
    for i in range(len(coins) - 1, -1, -1):
        temp = value/coins[i]
        value %= coins[i]
        coinCount += temp
        dictionaryCount[coins[i]] = temp
    return dictionaryCount, coinCount


coins = [1,2,4,8]

results = changeGreedy2(coins, 15)

print results