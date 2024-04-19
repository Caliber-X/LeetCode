class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1;
        int j = n-1;
        int tot = m+n-1;
        // for (int pos=tot; pos>=0; pos--) {
        while (tot >= 0) {
            // std::cout << "pos=" << pos << " i=" << i << " j=" << j << " -> ";
            if (j == -1)
                break;
            if (i == -1 || nums1[i] < nums2[j]) {
                // nums1[pos] = nums2[j--];
                nums1[tot--] = nums2[j--];
            }
            else {
                // nums1[pos] = nums1[i--];
                nums1[tot--] = nums1[i--];
            }
            // for (int _pos=0; _pos<=tot; _pos++)
            //     std::cout << nums1[_pos] << " ";
            // std::cout << std::endl;
        }
    }
};