


class Solution {
    //Attempting the Two-Pointer Solution
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length; 
        int p1 = 0; 
        int p2 = n - 1; 

        for(;;){
            int sum = numbers[p1] + numbers[p2]; 
            if(sum > target) {
                p2 -= 1 ;
            }
            else if(sum < target){
                p1 += 1; 
            } 
                
            else return new int[]{p1 +1, p2 +1}; 
        }
    }
}
