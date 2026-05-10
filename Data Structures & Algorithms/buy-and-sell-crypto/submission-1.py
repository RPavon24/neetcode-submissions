class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute force: go through every possible transaction

        #Solution:
        left = 0 #buy
        maxProfit = 0

        for i in range(1, len(prices)): 
            sale = prices[i] - prices[left]
            if(sale < 0): #there exist a low
                left = i  #update our left to be the new low
            elif (sale > maxProfit): 
                maxProfit = sale


        return maxProfit



