class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sDict ={} #initializing dictionary for string s

        tDict= {} #initializing dictionary for string t

        if len(s) != len(t):    #if the length of s does not equal to the length of t, then simply return false, this is a edgecase
            return False

        for char in s:          #for loop for every character in string S
            if char in sDict:           #if the character is a key in the dictionary already
                sDict[char] = sDict.get(char) + 1       #update this dictionary by adding 1 to the key value
            else:       #if the character is not a key in the dictionary already
                sDict[char] = 1     #simply initialize the char as a key in the dictionary with a value of 1

        for char in t:          #same as above
            if char in tDict:
                tDict[char] = tDict.get(char) + 1
            else:
                tDict[char] = 1

        return tDict == sDict       #return boolean value of tDict equals to sDict, if equal, returns true, else returns false, this compares keys and values
    
    #Time Complexity is O(n) aka linear