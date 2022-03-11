class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            tf = True
            x = i
            while x > 0:
                temp = x%10
                if temp == 0:
                    tf = False
                    break
                if i % temp != 0:
                    tf = False
                    break
                x = int(x/10)
            if tf :
                ans.append(i)
        return ans