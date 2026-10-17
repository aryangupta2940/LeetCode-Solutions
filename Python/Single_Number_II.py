class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0

        for bit in range(32):
            count = 0

            for num in nums:
                if num & (1 << bit):
                    count += 1

            if count % 3 != 0:
                a |= (1 << bit)

        if a >= 2**31:
            a -= 2**32

        return a