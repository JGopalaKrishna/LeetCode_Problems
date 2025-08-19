class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        n=len(nums)
        i=0
        result=0
        while(i<n):
            zero=0
            while(i<n and nums[i]==0):
                zero+=1
                i+=1
            i+=1
            result+= zero * (zero + 1) // 2
        return result
        '''
        zero=0
        res=0
        for i in nums:
            if i==0:
                zero+=1
                res+=zero
            else:
                zero=0
        return res