class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            morsecode = ""
            for i in word:
                morsecode += Morse_code[ord(i)-ord("a")]
            ans.add(morsecode)
        return len(ans)