class Solution:

    def encode(self, strs: List[str]) -> str:
        """ <length> <delim> <str> : 3#cat"""
        result = ""
        for s in strs: 
            n = len(s)
            result += str(n) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        if len(s) == 0: 
            return list()
        i = 0
        strs = []
        while True:
            if i >= len(s): 
                break
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            i = j + 1
            strs.append(s[i:i+str_len])
            i += str_len
        return strs

