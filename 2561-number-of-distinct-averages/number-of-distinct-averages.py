class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l=[]
        while(len(nums)):
            mi=min(nums)
            mx=max(nums)
            l.append((mi+mx)/2)
            nums.remove(mi)
            nums.remove(mx)
        return len(set(l))