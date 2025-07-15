class Solution:
    def isValid(self, word: str) -> bool:
        d=o=c=0
        if len(word)<3:
            return False
        for i in word:
            if i.isdigit():
                d=1
            elif i in "AEIOUaeiou":
                o=1
            elif i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                c=1
            else:
                return False
        return((o==1 and c==1))