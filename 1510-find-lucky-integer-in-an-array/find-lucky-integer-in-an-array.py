class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # d={}
        # for i in arr:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # res=-1
        # for k,v in zip(d.keys(),d.values()):
        #     if k==v and res<k:
        #         res=k
        # return res
        res=-1
        for n in set(arr):
            if n==arr.count(n) and res<n:
                res=n
        return res