__author__ = 'Andrew.Brown'

##############################################################
# changeDP(coinValueList, value)
# uses the dynamic programming approach to solve the min coin problem in O(nA) running time
# inputs: an array containing denominations of coins, an int to find change for
# returns: a tuple containg array with count of coins used, and the final answer
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
	#list to be filled by getCoins function
    newList = [0]*len(coinValueList) 
    getCoins(len(coinValueList)-1, value, coinValueList, coinsUsed, newList)
    return (newList, minCoins[len(coinValueList)-1][value])



##############################################################
# getCoins(i, j, denom, used, returnThis)
# This function will fill the returnThis array with the number of times each denomination has been used
# inputs: length of coin denomination list, value of change needed, coin denomination list, coinsUsed array, and array to be filled with counts of denoms used
# returns: n/a, uses reference to fill the returnThis
def getCoins(i, j, denom, used, fill_This):
    if j < 0 or i < 0:
        return
 
    #if current denom was used at least once in this spot
    if used[i][j] >0:
        fill_This[i] +=1
        if j-denom[i]<denom[i]:
            #change denomination.
            getCoins(i-1, j-denom[i], denom, used, fill_This)

        else:
            #same denomination
            getCoins(i, j-denom[i], denom, used, fill_This)
 
	#if current denom no longer used, go to next denom
    else:
        getCoins(i-1, j, denom, used, fill_This)


##############################################################
# changeGreedy(coins, value)
# This function uses the linear approach to solve the min coin problem
# however since it is "greedy" ie always starts with highest coin values, can result in higher "minumum" than other algorithms
# inputs: an array containing coin denominations, an int containing value to find change for
# returns: an array with a count of how many times each denomination was used, and an int with the sum
def changeGreedy(coins,value):
    pocket = [0] * len(coins)
    sum = 0
    #start with highest value coin (assumes sorted array of denominations)
    for i in range((len(coins)-1), -1, -1):
        temp = value/coins[i]
        pocket[i] += 1
        value -= coins[i] * temp
        if temp != 0:
            sum +=1

    return (pocket,sum)  





coins = [1,2,4,8]

results = changeDP(coins, 15)

print results