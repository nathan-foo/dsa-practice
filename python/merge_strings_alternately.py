class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr = []
        length = len(word1) if len(word1) <= len(word2) else len(word2)

        for i in range(length):
            arr.append(word1[i])
            arr.append(word2[i])

        if (len(word1) > len(word2)):
            while length < len(word1):
                arr.append(word1[length])
                length += 1
        elif (len(word2) > len(word1)):
            while length < len(word2):
                arr.append(word2[length])
                length += 1
        
        return "".join(arr)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        out = []
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                out.append(word1[i])
            if i < len(word2):
                out.append(word2[i])
            i += 1
        return "".join(out)