class Solution {
public:
    static int minOperations(vector<int>& nums) {
        const int n = nums.size();
        int i0 = -1, op = 0;

        while (i0 < n - 2) {
            i0 = find(nums.begin() + i0 + 1, nums.end(), 0) - nums.begin();
            if (i0 >= n - 2)
                break; // If no 0 is found or we are at the end
            nums[i0 + 1] = !nums[i0 + 1];
            nums[i0 + 2] = !nums[i0 + 2];
            op++;
        }

        // Handle the cases when we are near the end of the array
        return (i0 >= n) ? op : -1;
    }
};

auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();