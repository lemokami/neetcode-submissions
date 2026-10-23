class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        charSArr = [0] * 26

        for ch in s:
            charSArr[ord(ch)-97] += 1
        
        for ch in t:
            charSArr[ord(ch)-97] -= 1
        

        for count in charSArr:
            if count < 0 or count > 0:
                return False
            
        
        return True

