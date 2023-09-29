class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        monodecreasing = True       #setting monodecreasing to a boolean variable true

        monoincreasing = True       #setting monoincreasing to a boolean variable true

        for i in range(1, len(nums)):       #for loop, starting at 1 since i want to check the num behind, if we start at 0 we will encounter error
            if nums[i] > nums[i-1]:         #if nums[i] is greater than nums[i-1] then monodecreasing is false obviously, 
                monodecreasing = False
            elif nums[i] < nums[i-1]:       #if nums[i] is less than nums[-1] then monoincreasing is false obviously
                monoincreasing= False

            if not monodecreasing and not monoincreasing:       #if both monodecreasing and monoincreasing are false, that means it went through both phases, so return false 
                return False

        
        return monodecreasing or monoincreasing     #at the end of the for loop, return monodecreasing or monoincreasing, if either are true then that means its good


