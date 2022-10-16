#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct node{
int data;
node*left,*right;
};

node* constructbst(int high, node *head, vector<int> v, int low)

{
    
    if(low>high)
    {
        return NULL;
    }
   

  int mid=(low+high)/2;  
head->data=v[mid];
head->left = constructbst(high, head, v, mid + 1);
head->right = constructbst(mid - 1, head, v, mid - 1);
return head;
    
   
 }
 void inorder(node*root)
 {
if(root!=NULL)
{
    inorder(root->left);
    cout<<root->data;
    inorder(root->right);
}
 }
int main()
{
node*root=NULL;
int n;
cin>>n;
vector<int>v;
for(int i=0;i<n;i++)
{
    int r;
    cin>>r;
    v.push_back(r);
}
root=constructbst(n,root,v,0);
inorder(root);
}