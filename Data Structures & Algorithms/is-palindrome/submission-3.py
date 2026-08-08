class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        while(l<r):
            if not s[l].isalnum():
                while( l<r and (not s[l].isalnum())):
                    l+=1

            if not s[r].isalnum():
                while( l<r and (not s[r].isalnum())):
                    r-=1

            if  not (s[l].lower() == s[r].lower()):
                return False
            l+=1
            r-=1
        return True