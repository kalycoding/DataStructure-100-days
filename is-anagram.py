class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagramMap = {}
        for i in s:
            anagramMap[i] = anagramMap.get(i,0)+1
        
        for i in t:
            anagramMap[i] = anagramMap.get(i,0)-1
            
        for v in anagramMap.values():
            if v != 0:
                return False
        return True