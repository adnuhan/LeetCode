class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        output = ""
        transformation = []


        for word in words:
            for letter in word:
                output += morse_code[ord(letter) - 97]
            if output not in transformation:
                transformation.append(output)
            output = ""

        return(len(transformation))
        