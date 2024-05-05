# ORIGINAL ANSWER, CANNOT PASS LAST 2 TEST CASES BECAUSE OF THE MEMORY LIMIT
# COS IT IS A BANG BANG METHOD


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max = 0
#         for i in range(len(prices)):
#             for j in range(len(prices)):
#                 if i != j and j > i:
#                     sell = prices[j]
#                     buy = prices[i]

#                     print(sell, buy, sell-buy)
#                     if sell - buy > max:
#                         max = sell-buy
#         return max
    
# BETTER SOLUTION USING KATANADE ALGORITHM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            elif prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
        return max_profit
    

l = [2,4,1]
s = Solution()
m = s.maxProfit(l)
print(m)