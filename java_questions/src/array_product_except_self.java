import java.util.Arrays;

public class array_product_except_self {

/*
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Please solve it without division
 */

    public static void main(String[] args){

        int[] test = {1,2,3,4,5,6,7};

        productExceptSelf(test);

    }


    private static int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] small = new int[len];
        int[] big = new int[len];
        small[0] = 1;
        big[len - 1] = 1;

        for(int i = 1; i < len; i++) {
            small[i] = nums[i-1] * small[i-1];
        }

        for(int i = len - 2; i >= 0; i--) {
            big[i] = nums[i+1] * big[i+1];
        }

        for(int i = 0; i < len; i++) {
            small[i] *= big[i];
        }
        return small;
    }


    private static int[] productExceptSelfinefficient(int[] input){

        int[] output = new int[input.length];


        for (int i = 0; i<input.length; i++){
            int sum = 1;
            for (int j = 0; j<output.length; j++){
                if (j != i){
                    sum = sum* input[j];
                }
            }

            output[i] = sum;
        }
        System.out.println(Arrays.toString(output));
        return output;
    }

}
