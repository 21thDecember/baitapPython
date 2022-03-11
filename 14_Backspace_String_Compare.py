class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def BSC(string):
            ans = ""
            for i in string:
                if i == "#" and len(ans) > 0:
                    ans = ans[:-1]
                elif i != "#":
                    ans+=i
            return ans
        if BSC(s)==BSC(t) : 
            return True
        return False