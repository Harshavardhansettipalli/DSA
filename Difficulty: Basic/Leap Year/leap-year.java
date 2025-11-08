// User function Template for Java

class Solution {
    static boolean isLeap(int N) {
        // code here
       if ((N % 4 == 0 && N % 100 != 0) || (N % 400 == 0)) {
            return true;
        } else {
            return false;
        }
    }
}