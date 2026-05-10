class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 2) return new int[]{0,1}; //Basic Solution

        HashMap<Integer, Integer> set = new HashMap<>(); 
        int j = 0; 
        int i = 0;        
        for(int k = 0; k < nums.length; k++){
            int difference = target - nums[k]; 
            if(set.containsKey(difference)){
                j = set.get(difference); //index of value that's equal to difference
                i = k; 
                break; 
            }
            else{
                set.put(nums[k], k); 
            }
        }

        int[] solution = new int[]{i, j}; 
        Arrays.sort(solution); 
        return solution; 
    }
}