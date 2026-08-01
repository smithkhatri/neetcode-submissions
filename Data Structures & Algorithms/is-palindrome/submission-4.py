class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        
        loop through half

        check if i is valid or not
        if it is compare with j

        loop until you find valid i and j, and then compare, then repeat

        """
        i = 0
        j = len(s) - 1
        while i < j:
            while True and i<j:
                if 'a' <= s[i].lower() <= 'z' or '0' <= s[i] <= '9':
                    ii = s[i].lower()
                    break
                else:
                    i += 1

            while True and i<j:
                if 'a' <= s[j].lower() <= 'z' or '0' <= s[j] <= '9':
                    jj = s[j].lower()
                    break
                else:
                    j -= 1

            if s[i].lower() == s[j].lower():
                pass
            else:
                return False
                    

            i += 1
            
            j -= 1

        return True
    


