class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(","}": "{","]": "[",}
        a = []
        for i in s:
            if i in pair.values():
                a.append(i)
            elif i in pair.keys():
                if not a or a[-1] != pair[i]:
                    return False
                a.pop()
        return not a
