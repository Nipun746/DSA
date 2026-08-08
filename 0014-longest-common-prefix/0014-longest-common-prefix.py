class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        # """
        minimum = float('inf')

        for s in strs:
            if len(s)<minimum:
                minimum = len(s)
        i = 0 
        while i < minimum:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1 
        return s[:i]