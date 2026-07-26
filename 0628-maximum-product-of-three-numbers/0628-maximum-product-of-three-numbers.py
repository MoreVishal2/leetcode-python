class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n1=float('-inf')
        n2=float('-inf')
        n3=float('-inf')

        m1=float('inf')
        m2=float('inf')

        for i in nums:
            if i>n1:
                n3=n2
                n2=n1
                n1=i
            elif i>n2:
                n3=n2
                n2=i
            elif i>n3:
                n3=i

            if i<m1:
                m2=m1
                m1=i
            elif i<m2:
                m2=i


        return max(n1*n2*n3,n1*m1*m2)