class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_tracker = {}
        t_tracker = {}
        
        for ch in s:
            s_tracker[ch] = s_tracker.get(ch, 0) + 1
           
        for ch in t:
            t_tracker[ch] = t_tracker.get(ch, 0) + 1
            
        for ch in s:
            if s_tracker.get(ch,0) != t_tracker.get(ch,0):
                return False
            
        return True