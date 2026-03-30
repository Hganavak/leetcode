class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        print('sorted', nums)

        if len(nums) <= 2:
            return nums[0]

        # len 3 -> 2
        # 1 3 3
        # 1 1 3

        # len 4 -> 2
        # 1 2 2 2
        
        return nums[len(nums) // 2 ]