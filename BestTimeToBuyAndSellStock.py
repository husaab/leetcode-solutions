class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        min = prices[0] #initializing min as prices 0
        maxprofit =0 #initializing maxprofit
        
        counter =1 #initializing a counter so no need to do for loop


        while counter < len(prices):

            if prices[counter] < min:   # if prices[counte] is less than min
                min = prices[counter]       #than min is equal to prices counter
            if prices[counter] - min > maxprofit: #we check here if prices[counter] - min is greater than profit
                maxprofit = prices[counter] - min       # than maxprofit becomes prices[counter] - min become maxprofit

            counter=counter+1   #at end of both if statements we will increase counter by 1
        
        #the way this works is that min will always be behind counter, so it only checks prices ahead
        
        return maxprofit
        