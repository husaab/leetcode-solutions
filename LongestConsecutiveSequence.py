class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        maxcount=0  #initializing maxcount
        set_nums= set(nums) #initializing set of numbers

        for num in set_nums:        #looping through set
            if num-1 not in set_nums:       #if num-1 is not in set, that means it can be start of sequence
                tempcount=1    #temp count =1
                while(num+tempcount in set_nums): #while num + tempcount is in set nums, so while sequence
                    tempcount+=1        #add 1 to tempcount
                if tempcount > maxcount:        #at the end of the while loop, if temp count > maxcount
                    maxcount=tempcount      #than maxcount = tempcount

        return maxcount     #simply return maxcount by the end

        #Time complexity is O(n) where n is looping through the array
