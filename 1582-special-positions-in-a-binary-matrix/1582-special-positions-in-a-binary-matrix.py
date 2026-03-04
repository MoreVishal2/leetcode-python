class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l_r=[0]*len(mat)
        l_c=[0]*len(mat[0])

        for i in range(len(l_r)):
            for j in range(len(l_c)):
                if mat[i][j]==1:
                    l_r[i]+=1
                    l_c[j]+=1

        count=0
        for i in range(len(l_r)):
            for j in range(len(l_c)):
                if l_r[i]==1 and l_c[j]==1 and mat[i][j]:
                    count=count+1

        return count