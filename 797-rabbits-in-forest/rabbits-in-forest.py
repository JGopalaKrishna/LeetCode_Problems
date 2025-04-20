class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #re=0
        #for i in set(answers):
            #re+= math.ceil( answers.count(i) / (i+1) ) *(i+1)
        #return re
        return sum(math.ceil(answers.count(i) / (i + 1)) * (i + 1) for i in set(answers))
