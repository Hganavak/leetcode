class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        best=1
        nums = list(set(nums))
        nums.sort()

        l=0
        r=1

        cur_count=1
        for r in range(len(nums)):
            if nums[r] == nums[l] + 1:
                cur_count += 1
                best = max(best, cur_count)
                l += 1
            else:
                cur_count = 1
                l = r

        return best