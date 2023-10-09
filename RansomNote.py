class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazinelist= []        #initialize list where we store magazinelist in it

        for char in magazine:       #for char in magazine
            magazinelist.append(char)       #append  it to the list

        

        for char in ransomNote:     #for char in ransomnote
            if char in magazinelist:        #if the cahracter is in magazinelist
                magazinelist.remove(char)       #remove it from magazinelist
            else:              #if char not in magazine list, simply return false
                return False
        
        return True     #by the end, we will return true 
    
    #Time complexity is O(n), this isn't the most optimal solution, we can achieve better runtime and others but I also like thinking of unique solutions
            
            