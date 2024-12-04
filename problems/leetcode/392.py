class Solution:
    def isSubsequence(self, sub: str, word: str) -> bool:
        if len(sub) > len(word):return False
        if len(sub) == 0:return True
        subsequence = 0
        for i in range(0,len(word)):
            if subsequence < len(sub):
                if sub[subsequence] == word[i]:
                    subsequence += 1
        return subsequence == len(sub)
      
