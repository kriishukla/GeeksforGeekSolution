//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution{
    public:
    int maxOnes(int arr[], int n)
    {  
        int cnt0=0;
        int maxZero=0;
        int cnt1=count(arr,arr+n,1);
        
        for(int i=0;i<n;i++){
            if(arr[i]==0)cnt0++;
            else if(cnt0>0)cnt0--;
            maxZero=max(maxZero,cnt0);
        }
        return cnt1+maxZero;
    }
};


//{ Driver Code Starts.
int main()
{
    int t; cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n+5];
        for(int i=0;i<n;i++)
            cin>>a[i];
        Solution ob;
        cout<< ob.maxOnes(a, n) <<endl;
    }
    return 0;
}

// } Driver Code Ends