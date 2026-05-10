class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping: anagram -> anagram list
        hashMap = {}
        for s in strs: 
            sList = str(sorted(s))
            if sList not in hashMap: 
                hashMap[sList] = [s]
            else: 
                hashMap[sList].append(s)
        result = []
        for sList in hashMap: 
            result.append(hashMap[sList])
        
        return result