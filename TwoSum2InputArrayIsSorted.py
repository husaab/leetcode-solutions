class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0 #initializing start
        end = len(numbers)-1 #initializing end

        while start != end:     #while start does not equal to end, since we cant return same element
            
            currentsum = numbers[start] + numbers[end]      #current sum is numbers[start] + nums[end]

            if currentsum > target: # if current sum is greater than target than reduce end by 1
                end-=1
            elif currentsum < target:       #elif current sum less than target than increase start by 1
                start+=1
            else:
                return [start+1, end+1]    #else, that means currentsum is equal to target, return them both

        





        
        