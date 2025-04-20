class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        re=0
        for i in set(answers):
            c=answers.count(i)
            re= re + ( ( math.ceil( c / (i+1) ) ) * (i+1) )
        return re