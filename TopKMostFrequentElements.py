class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        storenums = {}      #initialize dictionary to store nums and their count

        for num in nums:        #for loop for every number in numbers
            if num in storenums:        #if number in storenums as a key already
                storenums[num] +=1      #just add 1 to the value
            else:       #if number is not in storenums as a key
                storenums[num] = 1 #initialize it as a key and add the first count (1)

        # for loop above is for the count of each number

        result =[]      #create a list called result

        
        for _ in range(k):      #for _ in range k, we will check the top k most frequent elements

            max_key = max(storenums, key=storenums.get)     #get the key with the max value
            result.append(max_key)                          #append the key with the max value
            del storenums[max_key]                          #now, delete the key with the max value from the dictionary

        return result       #return the result list with the top k most frequent elements
    

#Time complexity is O(n * k) n is is the key from the dictionary and k is the int given
        