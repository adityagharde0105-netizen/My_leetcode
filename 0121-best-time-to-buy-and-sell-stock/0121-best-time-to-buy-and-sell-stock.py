class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        best = 0

        for price in prices[1:]:
            least = min(price, least)
            profit = price - least
            best = max(best, profit)
        return best
       

    

        