class Solution:
    def maxProduct(self, n: int) -> int:
    a=list(str(n))
    a=[int(x) for x in a]
    a.sort(reverse=True)
    return a[0]*a[1]