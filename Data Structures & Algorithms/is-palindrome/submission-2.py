class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal= ''
        s=s.lower()
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for i in s:
            if i in alpha:
                pal += i

        return pal == pal[::-1]