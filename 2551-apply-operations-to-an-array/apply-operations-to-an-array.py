class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                nums[i-1]*=2
                nums[i]=0
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        return nums;