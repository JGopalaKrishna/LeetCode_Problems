class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        for i in set(answers):
            d[i]=answers.count(i)
        re=0
        for i in d.keys():
            re= re + ( ( math.ceil( d[i] / (i+1) ) ) * (i+1) )
        return re

        