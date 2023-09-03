class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a=0;
        int b=0;

        for (int i=0;i<nums.length-1;i++){
            a=i;
            
                for (int j=i+1;j<nums.length;j++){
                    
                    
                    b=j;
                    if (nums[j]==target-nums[i]){
                        int[] lists={a,b};
                        return lists;
                    }
                    
                }
            
            }
        int[] lists={a,b};
        return lists;
        }
        
    }

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1, -2, -3, -4, -5};
        int target = -8;
        int[] result = solution.twoSum(nums, target);

        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}