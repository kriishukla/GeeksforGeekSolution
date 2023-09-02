//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
    public:
    //Complete this function
    
     void solve(vector<string> &ans,int start,int end,string S) {
        if(start>=end)
        {
            ans.push_back(S);
            return ;
        }
        
        else {
            for(int i = start;i<end;i++) {
                swap(S[i],S[start]);
                solve(ans,start+1,end,S);

                swap(S[i],S[start]);
            }
        }
    }
    
    
    vector<string> permutation(string S)
    {
        //Your code here
        vector<string> ans;
        solve(ans,0,S.size(),S);
        sort(ans.begin(),ans.end());
        return ans;
    }
};


//{ Driver Code Starts.

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		string S;
		cin>>S;
		Solution ob;
		vector<string> vec = ob.permutation(S);
		for(string s : vec){
		    cout<<s<<" ";
		}
		cout<<endl;
	
	}
	return 0;
}
// } Driver Code Ends