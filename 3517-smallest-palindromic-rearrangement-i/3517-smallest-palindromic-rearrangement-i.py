class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            if freq[i] > 0:
                ch = chr(i + ord('a'))
                left.append(ch * (freq[i] // 2))

                if freq[i] % 2 == 1:
                    mid = ch

        left = "".join(left)

        return left + mid + left[::-1]