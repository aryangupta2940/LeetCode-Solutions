class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in lookup:
                return [lookup[needed], i]
            lookup[num] = i
