class Solution:

    """
    Encode: (length of string) # (string)

    Decode: check for number, if number trails with #, then read that no. of strings after #, move to new pointer (previous + n)

    """

    """
    ["Hello", "World"] -> 5#Hello5#World

    ["Ab#Hi4#", "Apple", "Cat" ] -> 

    -> 199#
    """

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for i in strs:
            encoded_str = encoded_str + str(len(i)) + '#' + str(i)   
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        ans = []

        pointer = 0
        "7# Ab#Hi4# 5# Apple 3# Cat"
        for i in range(len(s)):
            if s[i] == '#':
                try:
                    n = int(s[pointer:i])
                    ans.append(s[i+1:i+1+n])
                    pointer = i+1+n
                except:
                    continue
        return ans


                






























        