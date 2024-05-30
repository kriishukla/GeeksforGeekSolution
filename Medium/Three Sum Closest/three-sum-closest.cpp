//{ Driver Code Starts
//Initial function template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

// arr : given vector of elements
// target : given sum value

class Solution{
  public:
int threeSumClosest(vector<int> nums, int X) {
        sort(nums.begin(),nums.end());
        int ans=-1;
        int minAbsDiff=INT_MAX;
        int n = nums.size();
        for(int i=0;i<n;i++){
            
            if(i>0 && nums[i]==nums[i-1]) continue;
              
            int j=i+1;
            int k=n-1;
            
            while(j<k){
                int sum=nums[i]+nums[j]+nums[k];
                if(sum==X){
                    return sum;
                }
                int currAbsDiff=abs(sum-X);
                if(currAbsDiff<minAbsDiff || (currAbsDiff==minAbsDiff && sum>ans)) {
                    minAbsDiff=currAbsDiff;
                    ans=sum;
                }
                if(sum<X) j++;
                else k--;
            }
        }
        return ans;
    }
};



//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while(t--) {
        
        int n,target;
        cin >> n >> target;
        
        vector<int> vec(n);
        
        for(int i = 0 ; i < n ; ++ i ) 
            cin >> vec[i];
        Solution obj;
        cout << obj.threeSumClosest(vec, target) << "\n";
    }
}

//Position this line where user code will be pasted.

// } Driver Code Ends