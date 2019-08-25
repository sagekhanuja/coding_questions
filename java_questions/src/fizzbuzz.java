import java.util.ArrayList;
import java.util.List;

public class fizzbuzz {

    public static void main(String[] args){
        fizzBuzz(42);
    }

    private static List<String> fizzBuzz(int n) {

        List<String> output = new ArrayList<String>();

        for (int i = 1; i<=n; i++){
            if (i%3 == 0 && i%5 == 0){
                output.add("FizzBuzz");
            }
            else if (i%5 == 0){
                output.add("Buzz");
            }
            else if (i%3 == 0){
                output.add("Fizz");
            }

            else{
                String i_value = String.valueOf(i);
                output.add(i_value);
            }

        }
        System.out.println(output.toString());
        return output;

    }

}
