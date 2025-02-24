class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiouAEIOU'
        maxC = curC = sum(1 for i in s[:k] if i in vowels)

        for i in range(k, len(s)):
            curC += (s[i] in vowels) - (s[i - k] in vowels)
            maxC = max(maxC, curC)
            if maxC == k:
                break
        
        return maxC
    