class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int l =0; int r =0;
    int     n = cardPoints.length;
        for(int i=0 ; i< k ; i++){
            l += cardPoints[i]; }
            int max = l;
            for(int i =0 ; i < k ; i++){
                l -= cardPoints[k-i-1];
                r += cardPoints[n-i-1];
                max = Math.max(max, l + r);
            }
            return max;
       
    }
}