class Solution:
    def strStr(self, haystack: str, needle: str) -> int:



        for i in range(len(haystack)):  #loops through haystack
            if haystack[i] == needle[0]:   # if haystack[i] is equal to the first char of needle
                if haystack[i:i + len(needle)] == needle: #check if haystack from i to i+len(needle)=needle
                    return i        #if it is, then simply return i
        
        return -1       #if it doesnt find needle at all simply return -1