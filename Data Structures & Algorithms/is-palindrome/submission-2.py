class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """
        convert everything to lowecase and no spaces

        Check for palindrome
            - i from 0
            - j from -1

            if i == j:
                continue
            else:
                break
                return False
            
            retur True
        
        "Was it a car or a cat I saw?"
        """

        new_s = ''
        for i in s:
            if 'a' <= i.lower() <= 'z' or '0' <= i <= '9':
                new_s += i.lower()
        
        s = new_s
        print(s)
        for i in range(int(len(s)/2)):
            if s[i] == s[len(s)-1-i]:
                continue
            else:
                return False
        return True



                



