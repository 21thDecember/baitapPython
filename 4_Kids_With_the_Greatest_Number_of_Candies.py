class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        Max =  max(candies)
        for i in candies:
            if i + extraCandies >= Max:
                ans.append(True)
            else:
                ans.append(False)
        return ans