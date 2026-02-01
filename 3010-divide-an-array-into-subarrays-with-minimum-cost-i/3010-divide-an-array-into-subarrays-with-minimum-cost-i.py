class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        fr=nums[0]
        sec=thr=float('inf')

        for i in range(1,len(nums)):
            if nums[i]<sec:
                thr=sec
                sec=nums[i]
            elif nums[i]<thr :
                thr=nums[i]

        return fr+sec+thr
            
        