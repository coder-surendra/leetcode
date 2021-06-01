def maxProfit(prices):
    profit = 0
    
    # checking if array is sorted in ascending order

    if(prices == sorted(prices)):
        return prices[-1] - prices[0]
    
    # checking if array is sorted in descending order
    if(prices  == sorted(prices,reverse=True)):
        return profit
    
    
    
    
    
    i = 1
    n = len(prices)
    while( i <  (n - 1) ):
        diff = prices[i] - prices[i-1]
        print('%d - %d = %d'%(prices[i] , prices[i-1] ,diff ))
        if(diff>0):
            profit += diff
        i += 1
    return(profit)

# arr = [7,1,5,3,6,4]
arr = [6,1,3,2,4,7]
print(maxProfit(arr))