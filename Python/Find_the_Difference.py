class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        for i in range(len(a)):
            if b[i] != a[i]:
                return b[i]
        return b[-1]