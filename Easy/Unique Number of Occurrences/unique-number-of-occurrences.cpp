//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution {
public:
    bool isFrequencyUnique(int n, int a[]) {
        unordered_map<int,int> primer;
        unordered_set<int> sieve;
        // First store all the elements in a map and their respective frequency
        for(int i=0; i<n; i++) {
            primer[a[i]]++;
        }
        // Then store all the frequecies in a set
        for(const auto &x: primer) {
            // If the element already exists return false
            if(sieve.count(x.second)>0) {
                return false;
            }
            sieve.insert(x.second);
        }
        return true;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        Solution ob;
        bool ans=ob.isFrequencyUnique(n,arr);
        if(ans)
            cout<<1<<endl;
        else
            cout<<0<<endl;
    }
}
// } Driver Code Ends