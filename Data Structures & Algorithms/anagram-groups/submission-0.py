from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = []
        for i in range(len(strs)):
            if i in seen:
                continue
            anagrams = []
            anagrams.append(strs[i])
            for j in range(i+1, len(strs)):
                if Counter(strs[i]) == Counter(strs[j]):
                    anagrams.append(strs[j])
                    seen.append(j)
            result.append(anagrams)
        return result
            
        



        