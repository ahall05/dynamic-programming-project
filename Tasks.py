# IMPORTANT
# The pseudocode in Milestone 2 was written using 1-based indexing for explanation purposes,
# in our implementation, we have switched to 0-based indexing for all tasks. All inputs,
# outputs, and test cases are written with this in mind.

def task1(A):
    # PROBLEM 1: BRUTE FORCE

    m = len(A)
    n = len(A[0])

    # result stores the information about the stock with the largest profit
    # found, initialized to zeros for the base case.
    # result = [stock, buy date, sell date, profit]
    result = [0, 0, 0, 0]

    # i tracks the stock, j1 tracks the buying day, j2 tracks the selling day
    # loop through every possibility, calculating profit and recording max along the way
    for i in range(m):
        for j1 in range(n - 1):
            for j2 in range(j1 + 1, n):
                profit = A[i][j2] - A[i][j1]
                if profit > result[3]:
                    result = [i, j1, j2, profit]

    return tuple(result)

#///////////////////////////////////////////////////////////////////////////////

def task2(A):
    # PROBLEM 1: GREEDY


    m = len(A)
    n = len(A[0])

    # result stores the information about the stock with the largest profit
    # found, initialized to zeros for the base case.
    # result = [stock, buy date, sell date, profit]
    result = [0, 0, 0, 0]

    # i tracks the outer stock loop, j tracks the inner price loop
    # lowest_price tracks the lowest price seen, LP_index tracks its day
    for i in range(m):
        # initialize lowest_price and its index to first day
        lowest_price = A[i][0]
        LP_index = 0
        for j in range(1, n):
            # calculate profit if we were to sell on day j
            profit = A[i][j] - lowest_price
            # if this is the best profit so far, update result
            if profit > result[3]:
                result = [i, LP_index, j, profit]
            # update lowest_price and its index if this is a cheaper buy day
            if A[i][j] < lowest_price:
                lowest_price = A[i][j]
                LP_index = j

    return tuple(result)

#///////////////////////////////////////////////////////////////////////////////

def task3(A):
    # PROBLEM 1: DYNAMIC PROGRAMMING
    
    m = len(A)
    n = len(A[0])
    
    # [stock_idx, buy_day, sell_day, max_profit]
    result = [0, 0, 0, 0]
    
    for i in range(m):
        min_day = 0
        for j in range(1, n):
            profit = A[i][j] - A[i][min_day]
            
            if profit > result[3]:
                result = [i, min_day, j, profit]
            
            # track cheapest buy day for the current stock
            if A[i][j] < A[i][min_day]:
                min_day = j
                
    return tuple(result)

#///////////////////////////////////////////////////////////////////////////////

def task6(priceMatrix, cooldownPeriod):
    # PROBLEM 3: DYNAMIC PROGRAMMING (Top-Down)
    
    stockCount = len(priceMatrix)
    totalDays = len(priceMatrix[0])
    
    # cache: day -> (max_profit, best_transactions)
    memoMap = [None] * totalDays
    
    def computeBestStartingAt(currentDay):
        # base case: out of bounds
        if currentDay >= totalDays:
            return (0, [])
            
        if memoMap[currentDay] is not None:
            return memoMap[currentDay]
            
        # option 1: skip today
        maxProfit, bestTxns = computeBestStartingAt(currentDay + 1)
        
        # option 2: buy today, sell on future day k
        for k in range(currentDay + 1, totalDays):
            for i in range(stockCount):
                tradeProfit = priceMatrix[i][k] - priceMatrix[i][currentDay]
                
                if tradeProfit > 0:
                    # enforce wait period before next buy
                    nextAvailableDay = k + cooldownPeriod + 1
                    futureProfit, futureTxns = computeBestStartingAt(nextAvailableDay)
                    currentTotal = futureProfit + tradeProfit
                    
                    if currentTotal > maxProfit:
                        maxProfit = currentTotal
                        bestTxns = [(i, currentDay, k)] + futureTxns
                        
        memoMap[currentDay] = (maxProfit, bestTxns)
        return memoMap[currentDay]
        
    finalProfit, finalSequence = computeBestStartingAt(0)
    return finalSequence


#///////////////////////////////////////////////////////////////////////////////

def task7(priceMatrix, cooldownPeriod):
    # PROBLEM 3: DYNAMIC PROGRAMMING
    print("implement")


