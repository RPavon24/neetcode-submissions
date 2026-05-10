class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 2) return new int[]{0,1}; //Basic Solution

        HashMap<Integer, Integer> set = new HashMap<>(); 
        int j = 0;      
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i]; 
            if(set.containsKey(difference)){
                j = set.get(difference); //index of value that's equal to difference 
                return new int[]{j, i};
            }
            else{
                set.put(nums[i], i); 
            }
        }
        return new int[]{}; 
    }
}