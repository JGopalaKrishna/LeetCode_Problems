class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=Counter(arr)
        res=-1
        for k,v in d.items():
            if k==v and res<k:
                res=k
        return res