__author__ = 'Andrew.Brown'


def changeDP(coinValueList,value):
    #create table for coinList * value
    minCoins = [[0 for x in range(value+1)]for x in range(len(coinValueList))]
    #fill first line of array with increments of 1
    for i in range(value+1):
        minCoins[0][i] = i

    returnThis = []

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

        returnThis.append(minCoins[i][j]/coinValueList[i])

    return (returnThis, minCoins[len(coinValueList)-1][value])


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

coins = [1,2,4,8]

results = changeDP(coins, 15)

print results