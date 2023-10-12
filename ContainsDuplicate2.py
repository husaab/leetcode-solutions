class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        storenums={} #storing a dictionary

        for i in range(len(nums)):      #for looping through nums
            if nums[i] in storenums and abs(i - storenums[nums[i]]) <= k: 
                # ^ checks if nums in dictionary and if abs of i - j is <= k
                return True     #return true
            else:       #if false,
                storenums[nums[i]] = i      #then we will update the dictionary for the nums