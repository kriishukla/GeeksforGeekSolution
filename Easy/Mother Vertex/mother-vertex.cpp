//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution 
{
    public:
  vector<int> vis;
    
    void dfs(int node, vector<int> adj[]) {
        vis[node] = true;
        for(int child: adj[node]) {
            if(vis[child]) continue;
            dfs(child, adj);
        }
    }
    
 int findMotherVertex(int n, vector<int>adj[]) {
     vis = vector<int>(n, false);
     int ans = -1;
     for(int i = 0; i < n; i++) {
         if(vis[i]) continue;
         dfs(i, adj);
         ans = i;
     }
     
     vis = vector<int>(n, false);
     dfs(ans, adj);
     
     for(int i = 0; i < n; i++)
         if(vis[i] == false) 
             return -1;
             
     return ans;
 }

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
		cin >> V >> E;
		vector<int>adj[V];
		for(int i = 0; i < E; i++){
			int u, v;
			cin >> u >> v;
			adj[u].push_back(v);
		}
		Solution obj;
		int ans = obj.findMotherVertex(V, adj);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends