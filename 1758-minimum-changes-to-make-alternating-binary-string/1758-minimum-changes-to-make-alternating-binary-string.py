class Solution:
    def minOperations(self, s: str) -> int:

        op1 = 0
        op2 = 0

        for i in range(len(s)):
            if s[i] != str(i % 2):
                op1 += 1
            if s[i] != str(1 - i % 2):
                op2 += 1

        return min(op1, op2)