class Solution {
    public int reverse(int x) {
        int count =0;
        while( x != 0){
           int rem = x%10;
          int  newcount = count*10 +rem;
           if((newcount -rem)/10 != count ) return 0;
           count = newcount;
           x/=10;
        }
        return count;
    }
}