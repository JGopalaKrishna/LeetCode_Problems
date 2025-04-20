class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        re=0
        for i in set(answers):
            c= math.ceil( answers.count(i) / (i+1) )
            re= re + (c * (i+1) )
        return re