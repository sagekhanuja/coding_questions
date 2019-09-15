import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class twosum {

    public static void main(String[] args){
        int[] test_nums = {1,2,3,5,4,3,2,3};
        int target = 5;
        TwoSum(test_nums,target);

    }


    private static int[] TwoSum(int[] nums, int target){

        Map<Integer, Integer> complements = new HashMap<>();

        for (int i = 0; i<nums.length; i++) {

            int this_complement = target - nums[i];
            if (complements.containsKey(this_complement)){

                int[] sol = new int[2];
                sol[0] = complements.get(this_complement);
                sol[1] = i;
                System.out.println(Arrays.toString(sol));
                return sol;

            }
            else{
                complements.put(nums[i], i);
            }

        }
        return new int[2];
    }

}
