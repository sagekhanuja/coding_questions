import java.util.ArrayList;
import java.util.List;

public class combination_sum {

    public static void main(String[] args){
        int[] test= {1,2,3,4,5};
        combinationSum(test, 7);

    }



    private static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> rs = new ArrayList<List<Integer>>();
        com(rs,new ArrayList<Integer>(),candidates,target,0,0);
        System.out.println(rs);
        return rs;
    }

    private static void com(List<List<Integer>> rs, List<Integer> s, int[] c, int t,int sum,int start){
        if(sum==t){
            List<Integer> ss = new ArrayList<Integer>(s);
            rs.add(ss);
            return;
        }
        if(sum>t) return;

        for(int i=start;i<c.length;i++){
            s.add(c[i]);
            com(rs,s,c,t,sum+c[i],i);
            s.remove(s.size()-1);
        }
    }








}
