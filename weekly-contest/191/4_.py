class Solution {
public:
    
    typedef long long ll;
    
    vector<int> nums;
    double fact[30];
    int sum;
    
    void dfs(int index, int count, int cl, int cr, double& ans1, double& ans2, double curans, double curans2) {
        if (count > sum/2) return;
        if (index == nums.size()) {
            if (count != sum/2) {
                return ;
            }
            ans1 += curans*curans2;
            if (cl == cr) ans2 += curans*curans2;
            return ;
        }
        for (int i = 0; i <= nums[index]; i++) {
            dfs(index+1, count+i, cl + (i>0), cr + (i < nums[index]), ans1, ans2, curans/fact[i], curans2/fact[nums[index]-i]);
        }
    }
    
    double getProbability(vector<int>& balls) {
        nums = balls;
        sum = 0;
        for (auto i: nums) sum += i;
        fact[0] = 1;
        for (int i = 1; i < 30; i++) fact[i] = fact[i-1]*i;
        double ans1 = 0, ans2 = 0;
        assert(sum % 2 == 0);
        dfs(0, 0, 0, 0, ans1, ans2, fact[sum/2], fact[sum/2]);
        return ans2/ans1;
    }
};