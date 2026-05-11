class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        n = len(nums)
        l, r = 0, n - 1 

        # Find pivot
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # Pick which segment to look inn
        pivot_point = l

        if pivot_point == 0 or (nums[pivot_point] <= target <= nums[n - 1]):
            l, r = pivot_point,  n - 1
        else:
            l, r = 0, pivot_point - 1 

        # Search
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1 
        

        return -1

        