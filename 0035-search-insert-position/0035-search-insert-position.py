class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
            
            if i==len(nums)-1:
                if nums[i]>target:
                    return i
                else:
                    return i+1