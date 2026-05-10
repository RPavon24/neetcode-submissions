class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charS = s.toCharArray(); 
        char[] charT = t.toCharArray(); 
        HashMap<Character, Integer> mapS = new HashMap<Character, Integer>(); 
        HashMap<Character, Integer> mapT = new HashMap<Character, Integer>(); 
        
        if(s.length() != t.length()){
            return false; 
        }

        for(int i = 0; i < s.length(); i++){
            if(!mapS.containsKey(charS[i])){
                mapS.put(charS[i], 1); 
            } else{
                int count = mapS.get(charS[i]); 
                mapS.put(charS[i], count + 1); 
            }

            if(!mapT.containsKey(charT[i])){
                mapT.put(charT[i], 1); 
            } else{
                int count2 = mapT.get(charT[i]); 
                mapT.put(charT[i], count2 + 1); 
            }
        }

        for(Character c : mapT.keySet()){
            if(!mapS.containsKey(c)){
                return false; 
            }
            if(!mapT.get(c).equals(mapS.get(c))){
                return false; 
            }
        }

        return true; 
    }
}
