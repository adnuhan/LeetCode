class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        output = []
        
        for x in image:
            reversed = x[::-1]
            inverted = []
            for num in reversed:
                print(num)
                if num == 0:
                    num = 1
                else:
                    num = 0
                inverted.append(num)
            output.append(inverted)
            inverted = []

        return output
