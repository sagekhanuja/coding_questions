import java.util.*;

public class phonelettercombinations {

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<>();
        }

        Map<Character, List<Character>> map = new HashMap<>();
        map.put('1', Collections.singletonList('1'));
        map.put('2', Arrays.asList('a', 'b', 'c'));
        map.put('3', Arrays.asList('d', 'e', 'f'));
        map.put('4', Arrays.asList('g', 'h', 'i'));
        map.put('5', Arrays.asList('j', 'k', 'l'));
        map.put('6', Arrays.asList('m', 'n', 'o'));
        map.put('7', Arrays.asList('p', 'q', 'r', 's'));
        map.put('8', Arrays.asList('t', 'u', 'v'));
        map.put('9', Arrays.asList('w', 'x', 'y', 'z'));

        List<String> list = new ArrayList<>();
        char[] array = new char[digits.length()];

        letterCombinations(digits, 0, array, list, map);

        return list;
    }

    private void letterCombinations(String digits, int i, char[] memo, List<String> list, Map<Character, List<Character>> map) {
        if (i == digits.length()) {
            list.add(new String(memo));
            return;
        }

        char number = digits.charAt(i);
        List<Character> letters = map.get(number);

        for (Character letter : letters) {
            memo[i] = letter;
            letterCombinations(digits, i + 1, memo, list, map);
        }
    }

}
