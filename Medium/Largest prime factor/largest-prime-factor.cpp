//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends

class Solution{
public: 
    long long int largestPrimeFactor(int N){
        // code here
        //Method 2: T.C=O(sqrt(N))  S.C=O(1)
        long long int num=0;
        for(int i=2;i*i<=N;i++){
            while(N%i==0){
                num=i;
                N=N/i;
            }
        }
        return N>1 ? N : num;
    }
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.largestPrimeFactor(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends