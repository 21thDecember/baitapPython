class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentences = sentence.split(" ")
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(sentences)):
            if sentences[i][0].lower() in vowel:
                sentences[i]+="ma"
            else:
                sentences[i] = sentences[i][1:]+ sentences[i][0] + "ma"
            sentences[i]+="a"*(i+1)
        return " ".join(sentences)