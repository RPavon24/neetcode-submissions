
class Solution {
    public int[] productExceptSelf(int[] nums) {
        HashMap<Integer, Integer> preffix = new HashMap<>(); // index, value
        HashMap<Integer, Integer> suffix = new HashMap<>();  // index, value


        for(int i = 0; i < nums.length; i++){
            int numToAdd = 1;  
            int j = i -1; 
            while(j > -1){
                numToAdd = nums[j] * numToAdd; 
                j--; 
            }
            preffix.put(i, numToAdd); 
        }

        for(int i = nums.length - 1; i > -1; i--){
            int numToAdd = 1; 
            int j = i + 1; 
            while(j < nums.length){
                numToAdd = nums[j] * numToAdd; 
                j++; 
            }
            suffix.put(i, numToAdd); 
        }
        int[] solution = new int[nums.length]; 
        for(int i = 0; i < nums.length; i++){
            solution[i] = preffix.get(i) * suffix.get(i); 
        }

        return solution; 
    }   
}  
