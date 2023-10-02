class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start =0 #initializing start
        end= len(nums)-1 # initializing end
        mid = (start + end) // 2        # initializing mid

        while start <= end:     # while start is less than or equal to end
            
            if(nums[mid] > target):     #if nums[mid] is greater than target
                end= mid -1     #end becomes mid-1
                mid = (start + end) // 2        #mid becomes (start + end) //2
            elif(nums[mid] < target):       #else if nums[mid] is less than target
                start=mid + 1       #start becomes mid + 1
                mid= (start + end) //2
            else:       #if nums[mid] is not less than or greater than target, that means its equal to target so simply return mid
                return mid
        
        return -1       #if start eventually becomes greater than end, then return -1 this in the case that target is not in the list
    

    # Time complexity is (log n) where n is the number of elements in list
        