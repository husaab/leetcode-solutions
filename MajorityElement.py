class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        countdict = {}      #initialzie dictionary

        for num in nums:        #loop through nums list 
            if num in countdict:        #if number is in countdict
                countdict[num]+=1       #then add 1 to curr value
            else:           #else
                countdict[num]=1        #add it to dictionary with value = 1
        
        return max(countdict, key=countdict.get)        #return the key with the max value