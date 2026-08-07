class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final = ""
        
        # if len(word1) == len(word2):
        for char1,char2 in zip(word1,word2):
                final = final + char1 + char2
        if len(word1)>len(word2):
            n = len(word2)
            final = final + word1[n:]
        if len(word2)>len(word1):
            n = len(word1)
            final = final + word2[n:]
        return final
        # elif len(word1)<len(word2):
            
        #         wordx2 = word2[:n]
        #         for char1,char2 in zip(word1,wordx2):
        #             final = final + char1
        #             final = final + char2
        #         final = final + word2[n:]
        #         return final
        # elif len(word1)>len(word2):
        #         n = len(word2)
        #         wordx1 = word1[:n]
        #         for char1,char2 in zip(wordx1,word2):
        #             final = final + char1
        #             final = final + char2
        #         final = final + word1[n:]
        #         return final