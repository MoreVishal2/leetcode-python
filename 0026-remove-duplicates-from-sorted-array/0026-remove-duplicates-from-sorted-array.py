class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count=1
        for i in range(1,len(nums)):
            #comparing with the previous element (count-1) and swapping the count
            if nums[count-1]<nums[i]:
                temp=nums[count]
                nums[count]=nums[i]
                nums[i]=temp
                count=count+1
        return count