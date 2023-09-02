//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution{
public:
    int maxIndexDiff(int arr[], int n) {
        // code here
        vector<int> lmin(n,0);
        vector<int> rmax(n,0);
        lmin[0] = arr[0];
        rmax[n-1] = arr[n-1];
        for(int i = 1 ; i < n ;i++) {
            lmin[i] = min(lmin[i-1],arr[i]);
            rmax[n-1-i] = max(rmax[n-i],arr[n-1-i]);
        }
        int i = 0 , j = 0;
        int ans = 0;
        while(i<n && j < n) {
            if(lmin[i] <= rmax[j]) {
                ans = max(ans,j-i);
                j++;
            }
            else {
                i++;
            }
        }
        return ans;
    }
};




//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.maxIndexDiff(a, n);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends