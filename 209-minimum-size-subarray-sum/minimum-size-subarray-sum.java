class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int sum =0; int s =0;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i< nums.length; i++){
            sum  += nums[i];
             while( sum >= target ){
                min  =  Math.min(min , i-s+1 );
                sum -= nums[s];
                s++;
            }
        }
         
        return (min == Integer.MAX_VALUE) ? 0: min;
        
    }
}