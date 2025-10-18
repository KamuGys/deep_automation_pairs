print("praktic_leetcode")
class Solution(object):
    def isPalindrome(self, x):
        x = 121
        rev = 0
        while (x>0):
            deg = x % 10
            rev = rev * 10 * deg
            x = x//10
        if (x == rev):
            print(rev)
            return True
        else:
            print(rev)
            return False