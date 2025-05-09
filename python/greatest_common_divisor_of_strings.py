class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        index = 0
        
        a = len(str1)
        b = len(str2)
        while (b != 0):
            temp = b
            b = a % b
            a = temp

        while (index < a and str1[index] == str2[index]):
            index += 1

        if index == 0:
            return ""

        check1 = index
        check2 = index
        
        while (check1 < len(str1)):
            if (str1[check1:check1+index] != str1[0:index]):
                return ""
            check1 += index

        while (check2 < len(str2)):
            if (str2[check2:check2+index] != str2[0:index]):
                return ""
            check2 += index
        
        return str1[0:index]
    
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b  
            return a

        gcd_num = gcd(len(str1), len(str2))

        candidate = str1[:gcd_num]
        can_1 = candidate * (len(str1) / gcd_num) == str1
        can_2 = candidate * (len(str2) / gcd_num) == str2
        
        if can_1 and can_2:
            return candidate

        return ""
