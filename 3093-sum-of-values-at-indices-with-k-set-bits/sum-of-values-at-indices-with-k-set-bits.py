class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        su=0
        for i in range(len(nums)):
            if(bin(i).count('1')==k):
                su+=nums[i]
        return su