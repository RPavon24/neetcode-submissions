class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = s.replace(" ", "").lower()

        p1 = 0
        p2 = len(str1) - 1
        done = False
        while not done and p1 < p2: 
            if not str1[p1].isalnum(): 
                p1 += 1
                continue
            if not str1[p2].isalnum(): 
                p2 -= 1
                continue
            if str1[p1] != str1[p2]: 
                return False
            if p1 == p2: 
                break
            p1 += 1
            p2 -= 1
        return True