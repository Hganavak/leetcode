class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 
        
        print('target', target)

        while r > l:
            sum=numbers[l] + numbers[r]
            print('\tl:', l, 'r:', r, 'sum:', sum)

            if sum == target:
                return [l + 1, r + 1]

            elif sum > target:
                print('\t\tsum > target')
                r -= 1

            elif sum < target:
                print('\t\tsum < target')
                l += 1

        print('Error: Did not find match')
        return [0, 0]