//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
private:
    int func(int i, int w, int val[], int wt[], vector<vector<int>>& dp){
        if(i<0)return 0;
        if(dp[i][w]!=-1)return dp[i][w];
        
        int take=-1e9;
        if(wt[i]<=w){
            take=val[i]+func(i,w-wt[i],val,wt,dp);
        }
        int nott=0+func(i-1,w,val,wt,dp);
        return dp[i][w]= max(take,nott);
    }
public:
    int knapSack(int n, int w, int val[], int wt[])
    {
        vector<int>prev(w+1,0);
        for(int i=0;i<n;i++){
            
            for(int l=0;l<=w;l++){
                int take=-1e9;
                if(wt[i]<=l){
                    take=val[i]+prev[l-wt[i]];
                }
                
                prev[l]= max(take,prev[l]);
            }
            
        }
        return prev[w];
        
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N, W;
        cin>>N>>W;
        int val[N], wt[N];
        for(int i = 0;i < N;i++)
            cin>>val[i];
        for(int i = 0;i < N;i++)
            cin>>wt[i];
        
        Solution ob;
        cout<<ob.knapSack(N, W, val, wt)<<endl;
    }
    return 0;
}
// } Driver Code Ends