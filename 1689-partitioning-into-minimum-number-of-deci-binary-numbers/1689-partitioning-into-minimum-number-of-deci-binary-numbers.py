class Solution:
    def minPartitions(self, n: str) -> int:
        dig=0

        for i in n:
            if int(i)> dig:
                dig=int(i)

            
        return dig