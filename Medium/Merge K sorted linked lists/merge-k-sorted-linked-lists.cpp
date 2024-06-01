//{ Driver Code Starts
// C++ program to merge k sorted arrays of size n each
#include <bits/stdc++.h>
using namespace std;

// A Linked List node
struct Node
{
	int data;
	Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};

/* Function to print nodes in a given linked list */
void printList(Node* node)
{
	while (node != NULL)
	{
		printf("%d ", node->data);
		node = node->next;
	}
	cout<<endl;
}

// } Driver Code Ends
/*Linked list Node structure

struct Node
{
	int data;
	Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};
*/ 

class Solution{
  public:
    //Function to merge K sorted linked list.
    Node* merge(Node* head1, Node* head2){
        Node *ptr1 = head1;
        Node *ptr2 = head2;
    
        Node *dummy = new Node(-1);
        
        Node *res = dummy;
        
        while (ptr1 != NULL && ptr2 != NULL)
        {
            if (ptr1->data >= ptr2->data)
            {
                res->next = ptr2;
                res = res->next;
                ptr2 = ptr2->next;
            }
            else
            {
                res->next = ptr1;
                res = res->next;
                ptr1 = ptr1->next;
            }
        }
        
        if (ptr1 != NULL)
        {
            res->next = ptr1;
        }
        if (ptr2 != NULL)
        {
            res->next = ptr2;
        }
        
        return dummy->next;
    }
    Node * mergeKLists(Node *arr[], int K)
    {
           // Your code here
          Node*root=arr[0];
          for(int i=1;i<K;i++)
          {
              root=merge(root,arr[i]);
          }
          return root;
    }
};




//{ Driver Code Starts.
// Driver program to test above functions
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
	   int N;
	   cin>>N;
       struct Node *arr[N];
       for(int j=0;j<N;j++)
        {
           int n;
           cin>>n;

           int x;
           cin>>x;
           arr[j]=new Node(x);
           Node *curr = arr[j];
           n--;

           for(int i=0;i<n;i++)
           {
               cin>>x;
               Node *temp = new Node(x);
               curr->next =temp;
               curr=temp;
           }
   		}
   		Solution obj;
   		Node *res = obj.mergeKLists(arr,N);
		printList(res);

   }

	return 0;
}

// } Driver Code Ends