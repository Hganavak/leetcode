class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dict
        d ={}

        # Loop over the nums
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # New array. Take the dict and convert to a list of tuples
        # [(1, 3), (2, 5)] etc
        a=list(d.items())

        # Then sort it a (by default it uses first value)
        a=sorted(a, key = lambda x: x[1])
        print('sorrted: ', a)

        # Then take the value from each tuple pair 
        a = [x[0] for x in a]
        print('array: ', a)

        return a[-k:]