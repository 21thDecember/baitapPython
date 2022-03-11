class Solution:
    def findComplement(self, num: int) -> int:
        ans = bin(num)[2:]
        ans = ans.replace('0','2')
        ans = ans.replace('1','0')
        ans = ans.replace('2','1')
        new_num = 0
        for i in range(len(ans)):
            new_num+=int(ans[i])*pow(2,(len(ans)-i-1))
        return new_num