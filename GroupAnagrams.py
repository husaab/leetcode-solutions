class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}       #creating a dictionary to store key and values

        for str in strs:        #looping for every string in the array of strings
            value= "".join(sorted(str))     #the value is the sorted version of the string, with anagrams, you can tell if words are anagrams if the sorted version of each other is equal, hence i use sort
            if value in dict:           #if this value is in the dictionary as a key
                dict[value].append(str)     #then simply append the string to the value of the key
            else:       #if it is not in the dictionary
                dict[value]=[str]       #then create it as a list value

        result =[]      #creating result list to return

        for key in dict:        #looping through keys in dictionary
            result.append(dict[key])        #append the value of the key to the result list


        return result
    


#Time complexity is O(n * k log k) where n is number of words in array and k is the length of the longest word