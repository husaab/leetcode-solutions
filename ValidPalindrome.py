class Solution:
    def isPalindrome(self, s: str) -> bool:

        #first we will have to for loop and convert into a checkpal string where it only includes letter


        checkpal = "" #initializing checkpal str, only adds alphanum

        for char in s:
            if char.isalnum():
                checkpal += char.lower()
            

        #we will check with 2 pointers
        
        
        start = 0       #initialize start variable
        end= len(checkpal) -1       #initialize end variable which is length of checkpal -1

        while(start < end):     #while start is less than end
            if(checkpal[start] != checkpal[end]):       #if the checkpal string at start is not equal to checkpal string at end, then not pal
                return False        #ret false
            start+=1        #else add 1 to start
            end-=1           #and minus 1 to end
        
        return True     #if while loop passes then return true
        
                
