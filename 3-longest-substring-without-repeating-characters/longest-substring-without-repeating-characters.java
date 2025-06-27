class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l =0;
        int max =0;
    Set<Character> hi = new HashSet<>();
        for(int i=0;i< s.length();i++){
          char c = s.charAt(i);
          while(hi.contains(c)){
            hi.remove(s.charAt(l));
            l++;
          }
          hi.add(c);
          max = Math.max(max, i - l+1);
        }
        return max;
    }
}