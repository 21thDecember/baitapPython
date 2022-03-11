class Solution:
    def reverseWords(self, s: str) -> str:
        list_ = s.split(" ")
        for i in range(len(list_)):
            list_[i] = list_[i][::-1]
        return " ".join(list_)