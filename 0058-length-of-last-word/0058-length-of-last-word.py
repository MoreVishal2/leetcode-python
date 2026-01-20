class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean_s=s.rstrip()
        for i in range(len(clean_s)):
            ch=clean_s[-(i+1)]
            if ch==" ":
                return i
                break
        return len(clean_s)