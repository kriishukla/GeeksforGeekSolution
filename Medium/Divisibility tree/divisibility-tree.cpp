//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
public:
    
    int ans=0;
    
    void dfs(int node,int par,vector<int> adj[],vector<int>& size){
        for(auto it:adj[node]){
            if(it==par) continue;
            dfs(it,node,adj,size);
            size[node]+=size[it];
            if(size[it]%2==0) ans++;
        }
    }
    
    int minimumEdgeRemove(int n, vector<vector<int>>edges){
        vector<int> adj[n];
        
        for(auto it:edges){
            adj[it[0]-1].push_back(it[1]-1);
            adj[it[1]-1].push_back(it[0]-1);
        }
        vector<int> size(n,1);
        dfs(0,-1,adj,size);
        return ans;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>>edges;
		for(int i = 0; i < n-1; i++){
			int x, y;
			cin >> x >> y;
			edges.push_back({x,y});
		}
		Solution obj;
		int ans = obj.minimumEdgeRemove(n, edges);
		cout << ans <<"\n";
	}
	return 0;
}

// } Driver Code Ends