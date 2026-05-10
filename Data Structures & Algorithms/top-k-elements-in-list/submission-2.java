
class Solution {
    public static int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> set = new HashMap<>(); // num, count

        for(int num: nums){
            int count = 0; 
            if(set.get(num) != null){
                count = set.get(num); 
            }
            set.put(num, ++count);
        }

        int[] solution = new int[k];
        for(int i = 0; i < k; i++){
            int max = 0;  
            int key = 0; 
            for(int num: nums){
                if(set.get(num) == null) continue; 
                if(set.get(num) > max){
                    max = set.get(num);
                    key = num;  
                }
            }
            solution[i] = key; 
            set.remove(key); 
        }

        return solution; 
    }

    public static void main(String[] args){
        int[] nums = {1,2,2,3,3,3}; 
        int k=2; 

        int[] answer = topKFrequent(nums, k); 
        for(int num : answer){
            System.out.println(num);
        }
    }
}
