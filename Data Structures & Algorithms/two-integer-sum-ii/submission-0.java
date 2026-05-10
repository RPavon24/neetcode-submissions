
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length; 
        int[] solution = new int[2]; 

        for(int i = 0; i < n; i++){
            int difference = target - numbers[i]; 
            for(int j = n - 1; j >= 1; j--){
                if(difference == numbers[j]){
                    solution[0] = i + 1; 
                    solution[1] = j + 1; 
                    return solution; 
                }
            }
        }


        return solution; 
    }
}
