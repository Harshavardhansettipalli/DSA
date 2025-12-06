class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int pos = nums.size();
        int start=0,end=nums.size()-1;
        while(start<=end){
            int mid = start+(end-start)/2;
            if(nums[mid]==target){
                return mid;
            }else if(nums[mid]>target){
                pos=mid;
               end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return pos;
    }
};