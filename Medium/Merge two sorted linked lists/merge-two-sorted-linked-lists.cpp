//{ Driver Code Starts
#include<iostream>
using namespace std;

/* Link list Node */
struct Node
{
    int data;
    struct Node *next;
    
    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

Node* sortedMerge(struct Node* a, struct Node* b);

/* Function to print Nodes in a given linked list */
void printList(struct Node *n)
{
    while (n!=NULL)
    {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}

/* Driver program to test above function*/
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;

        int data;
        cin>>data;
        struct Node *head1 = new Node(data);
        struct Node *tail1 = head1;
        for (int i = 1; i < n; ++i)
        {
            cin>>data;
            tail1->next = new Node(data);
            tail1 = tail1->next;
        }

        cin>>data;
        struct Node *head2 = new Node(data);
        struct Node *tail2 = head2;
        for(int i=1; i<m; i++)
        {
            cin>>data;
            tail2->next = new Node(data);
            tail2 = tail2->next;
        }

        Node *head = sortedMerge(head1, head2);
        printList(head);
    }
    return 0;
}

// } Driver Code Ends




 

/* Link list Node
struct Node {
  int data;
  struct Node *next;
  
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/
//Function to merge two sorted linked list.

Node* sortedMerge(Node* head1, Node* head2)  
{  
    Node* head=NULL;
    Node* tail=NULL;
    
    //run till head1 and head2 are not null
    while(head1 and head2)
    {
        if(head1->data<head2->data)
        {
            if(head==NULL)
            {
                head=head1;
                tail=head1;
            }
            else
            {
                tail->next=head1;
                tail=head1;
            }
            head1=head1->next;
        }
        else
        {
            if(head==NULL)
            {
                head=head2;
                tail=head2;
            }
            else
            {
                tail->next=head2;
                tail=head2;
            }
            head2=head2->next;
        }
    }
    
    //if head1 is not null and head2 is null
    while(head1)
    {
        if(head==NULL)
        {
            head=head1;
            tail=head1;
        }
        else
        {
            tail->next=head1;
            tail=head1;
        }
        head1=head1->next;
    }
    
    //if head1 is null and head2 is not null
    while(head2)
    {
        if(head==NULL)
        {
            head=head2;
            tail=head2;
        }
        else
        {
            tail->next=head2;
            tail=head2;
        }
        head2=head2->next;
    }
    
    return head;
}  

    // code here