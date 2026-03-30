class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)

        output=[0] * n
        prefix=[0] * n
        suffix=[0] * n

        prefix[0] = 1
        suffix[n-1] = 1

        # Compute prefix
        product=1
        for i in range(n):
            product *= nums[i]
            prefix[i] = product

        print('prefix: ', prefix)

        # Compute suffix
        product=1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            suffix[i] = product

        print('suffix: ', suffix)
        for i in range(n):
            prefix_product = 1 if i == 0 else prefix[i - 1] 
            suffix_product = 1 if i == n - 1 else suffix[i + 1]
            output[i] = prefix_product * suffix_product


        return output


        


        