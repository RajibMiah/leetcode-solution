class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = list(s)
        word.append('null')
        roman_num = {"I": 1 , "V":5 , "X" :10 , 'L':50 , 'C':100 , 'D':500 , "M": 1000 }
        result = 0

        while(len(word) >= 0):
            if word[0] in roman_num:
                if(word[word.index(word[0]) + 1] != 'null'):
                    if roman_num[word[0]] >= roman_num[word[word.index(word[0]) + 1]]:
                            result += roman_num[word[0]]
                            word.pop(0)  
                    else:
                        result += ( roman_num[ word[1]] -  roman_num[word[0]])
                        word.pop(0)
                        word.pop(0)  
                else:
                     result += roman_num[word[0]]
                     word.pop(0)   
            else:
                break    

        return result   