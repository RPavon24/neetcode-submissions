class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>(); 
        int topLength = 0; 
        for(int num : nums){
            numSet.add(num); 
        }

        for(int num : numSet){

            if(!numSet.contains(num - 1)){
                int currentNum = num; 
                int currentStreak = 1; 
                
                
                while(numSet.contains(currentNum + 1)){
                    currentStreak++; 
                    currentNum++; 
                }

                topLength = Math.max(topLength, currentStreak); 
            }
        }

        return topLength; 
    }
}
