class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        MaxValue=0
        MaxV=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:    
                MaxV+=nums[i]
            else:
                if MaxV > MaxValue:
                    MaxValue=MaxV
                MaxV=nums[i]
        if MaxV > MaxValue:
            return  MaxV
        else:
            return MaxValue