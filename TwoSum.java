class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> storenums = new HashMap<>(); //initialize a hashmap that stores an integer as key and value as key

        for(int i=0; i < nums.length; i++){     //for loop for int i till length of nums

            int searchfor = target -nums[i];        //searchfor value is the value of target- nums[i], we check if this value is availaible, if so, nums[i] + searchfor would equal to target
            
            if( storenums.containsKey(searchfor) ){         //check if the hashmap contains searchfor
                return new int[]{i, storenums.get(searchfor)};      //if it does then return the array with i and the searchfor value
            }
            
            storenums.put(nums[i], i);      //if the hashmap does not contain searchfor, then add the nums[i] and i to the hashmap
            
        }

        return new int[]{}; //if not possible to find 2 numbers to add up to target, return empty list
        
    }
}