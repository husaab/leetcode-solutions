class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        storenums= set() #creating a set to store numbers

        for num in nums:        #looping through nums array
            if num in storenums:    #check if num is already in set
                return True #if so, return true
            else:   #else, add it to set
                storenums.add(num)
        
        return False    #by the end of the for loop, if no num was in set, then return False

#Time complexity is O(n) aka linear
