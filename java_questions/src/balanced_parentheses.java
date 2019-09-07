import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class balanced_parentheses {


    public static void main(String[] args){
        String test = "[][][]]]]][][][][][][][][][]";

        System.out.println(balanced_parentheses(test));
    }


    private static boolean balanced_parentheses(String input) {

        Stack<Character> stack = new Stack<Character>();
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('{', '}');
        map.put('[', ']');
        map.put('(', ')');

        for (char i : input.toCharArray()) {
            if (i == '(' || i == '{' || i == '[') {
                stack.push(map.get(i));
            } else {
                if (stack.isEmpty()){ return false; }
                char check = stack.pop();
                if (check != i) {
                    return false;
                }
            }
        }

        return true;
    }
}