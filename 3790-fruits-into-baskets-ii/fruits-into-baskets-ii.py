class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for i in fruits:
            for b in baskets:
                if(i<=b):
                    baskets.remove(b)
                    break
        return len(baskets)