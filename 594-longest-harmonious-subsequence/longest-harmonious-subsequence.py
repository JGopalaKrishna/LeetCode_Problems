class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # dic1={}
        # for i in nums:
        #     if i in dic1:
        #         dic1[i]+=1
        #     else:
        #         dic1[i]=1
        # sd= dict(sorted(dic1.items()))
        # re=0
        # lk=list(sd.keys())
        # for i in range(1,len(lk)):
        #     if(lk[i]-lk[i-1]==1):
        #         su=sd[lk[i]]+sd[lk[i-1]]
        #         if(re<su):
        #             re=su
        # --------------------------------------
        se=sorted(set(nums))
        re=0
        for i in range(1,len(se)):
            if(se[i]-se[i-1]==1):
                sums=nums.count(se[i])+nums.count(se[i-1])
                if(sums>re):
                    re=sums
        return re