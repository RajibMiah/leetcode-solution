
def findingIndices(s , words):
    i , j = 0 , 0
    n = len(s)
    freq = {}
    total_words = []
    ans_idx = []
    for word in words:
        print(word)
        total_words += word 

    for char in total_words:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1        
    count = len(freq)
    temp = freq.copy()
    print(total_words)
    while( j < n):
      
        if s[j] in freq:
                temp[s[j]] -= 1
                if temp[s[j]] == 0:
                    count -= 1  

        if (j - i  + 1 > len(total_words) - 1 ): 
            if count == 0:
                ans_idx.append(i)
                print('==========found ============')
                temp = freq.copy()
                count = len(freq)
            i += 1
        j += 1
        print(s[i : j])   
        print("i" , i , 'j' , j)
    return ans_idx

# print(findingIndices("barfoothefoobarman", words = ["foo","bar"] )) # [0 , 9]
# print(findingIndices("wordgoodgoodgoodbestword" , words = ["word","good","best","word"] )) # []
print(findingIndices("barfoofoobarthefoobarman" , ["bar","foo","the"] )) #[ 6 , 9 , 12]