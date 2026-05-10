
class Solution {
    public static boolean isValid(String s) {
        char[] string = s.toCharArray(); 
        int n = string.length; 
        Stack<Character> stack = new Stack<>(); 
        
        for(char c : string){
            if(isClosing(c)){
                if(stack.isEmpty()) return false; 
                char next = stack.pop(); 
                if(!isOpening(next)) return false; 
                if(!arePair(next, c)) return false; 
                continue; 
            }
            stack.push(c); 
        }
        if(!stack.isEmpty()) return false; 
        return true ;        
    }

    private static boolean isClosing(char c){
        return switch (c) {
            case (')') -> true;
            case (']') -> true;
            case ('}') -> true;
            default -> false;
        };
    }
    private static boolean isOpening(char c){
        return switch (c) {
            case ('(') -> true;
            case ('[') -> true;
            case ('{') -> true;
            default -> false;
        };
    }

    private static boolean arePair(char c1, char c2){
        switch(c1){
            case ('(') -> {
                return c2 == ')';
            }

            case('[') -> {
                return c2 == ']';
            }

            case('{') -> {
                return c2 == '}'; 
            }

            default -> {
                return false;
            }
        }
    }

    public static void main(String[] args) {
        String s = "([{}])" ; 

        System.out.println("Is Valid: " + isValid(s)); 
    }
}
