class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute force: go through every possible transaction

        #Solution:
        # go through and find the numbers that can make some profit
        # there is some price in index > current, that is more expensive

        profit = set()
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                sale = prices[j] - prices[i]
                if (sale > 0):
                    profit.add(sale)
        
        if (len(profit) > 0): 
            return max(profit)
        else:
            return 0

