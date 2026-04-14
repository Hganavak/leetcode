class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        # Brute force

        if len(prices) == 1:
            return 0
        
        elif len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        
        l = 0
        while l < len(prices) - 1:

            r = l + 1

            print(f"{l=}, {r=}")
            while r < len(prices):
                profit = max(prices[r] - prices[l], 0)
                best = max(best, profit)
                print(f"\t {l=}, {r=}, {profit=}")
                r += 1
                
            l += 1



        return best
            

        
        