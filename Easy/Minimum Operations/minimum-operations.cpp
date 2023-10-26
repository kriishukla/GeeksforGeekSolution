//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
  public:
    int minOperation(int n)
    {
        int count = 1;
        
        while(n!=1)
        {
           if(n%2 == 1)
           {
               count++;
               n = n-1;
           }
           
           n = n/2;
           count++;
            
        }
        
       return count;
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
	        Solution ob;
	        cout<<ob.minOperation(n)<<endl;
	    }
}
// } Driver Code Ends