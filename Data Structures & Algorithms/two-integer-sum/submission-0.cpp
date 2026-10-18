class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        int difference;
        std::unordered_map<int,int> hashmap;
        for(int i=0;i<n;i++){ 
            difference = target-nums[i];
            if(hashmap.find(difference) != hashmap.end()){
                return {hashmap[difference],i};
            }
             hashmap[nums[i]] = i;
        }
      return {};
    }
};
