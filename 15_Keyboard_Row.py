class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        list_ = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        ans = []
        for i in words: 
            for j in range(3):
                if set(i.lower()) | list_[j] == list_[j]:
                    ans.append(i)
        return ans