class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dict
        d ={}

        # Loop over the nums
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # New array
        a=sorted(list(d.items()), key=lambda x: x[1], reverse=True)

        print(a)
      
        a = [x[0] for x in a]

        return a[:k]