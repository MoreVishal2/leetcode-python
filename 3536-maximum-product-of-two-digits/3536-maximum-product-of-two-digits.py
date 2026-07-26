class Solution:
    def maxProduct(self, n: int) -> int:
        d1=d2=float('-inf')
        m=n
        while m>0:
            d=m%10
            if d>d1:
                d2=d1
                d1=d
            elif d>d2:
                d2=d
            m=m//10

        return d1*d2