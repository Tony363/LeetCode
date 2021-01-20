class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        i = 0
        string = ""
        for c in t:
            if string == s:
                return True
            if c == s[i]:
                string += s[i]
                i += 1
        return string == s
