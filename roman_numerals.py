class Solution:
    def romanToInt(self, s: str) -> int:
        # initialize hashmap of roman numerals
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "CM":900,
            "CD":400,
            "XC":90,
            "XL":40,
        }
        # initialize IV and IX count and value count
        IVc = 0
        IXc = 0
        CM = 0
        CD = 0
        XC = 0
        XL = 0
        romanv = 0
        # linear scan and parse by string slicing
        for c1,c0,cn in zip(range(1,len(s)),range(len(s)-1),range(len(s))):
            # check 9
            if s[c0:c1+1] == "IV":
                IVc += 1    
            # check 4
            elif s[c0:c1+1] == "IX":
                IXc += 1
            elif s[c0:c1+1] == "CM":
                CM += 1
            elif s[c0:c1+1] == "CD":
                CD += 1
            elif s[c0:c1+1] == "XC":
                XC += 1
            elif s[c0:c1+1] == "XL":
                XC += 1
        s = s.replace("IV","")
        s = s.replace("IX","")
        s = s.replace("CM","")
        s = s.replace("CD","")
        s = s.replace("XC","")
        s = s.replace("XL","")
        for c in s:
            romanv += roman[c]
        print(romanv,IVc,IXc,CM,CD)
        romanv = romanv + (4*IVc) + (9*IXc) + (900*CM) + (400*CD)
        # add the key value from hashmap
        return romanv
if __name__ == "__main__":
    solution = Solution()
    solution.romanToInt("IIVXIV")   