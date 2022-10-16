#include <bits/stdc++.h>
using namespace std;
struct node
{
    int data;
    node *left, *right;
};
node *insertnode(int i)
{
    node *temp;
    temp = new node;

    temp->data = i;
    temp->left = temp->right = NULL;
    return temp;
}

int find(int s,node*root,int x)
{
    if(s==root->data)
    {
        return x;
    }
    if(s<root->data)
    {
       return find(s,root->left,++x);
    }
    else {
   return find(s,root->right,++x);
    }
}

int search(int s,int sd,node*root)
{
    if(root->data==s||root->data==sd)
    {
        if(root->left->data==s||root->right->data==sd)
        {
            return 1;
        }
        else if(root->left->data==sd||root->right->data==sd)
        {
            return 1;
        }
        else{
            int x=find(s,root,0);
            int y=find(sd,root,0);
            return x+y;
        }
    }
    if((s>root->data&&sd<root->data)||s<root->data&&sd>root->data)
    {
    int x=find(s,root,0);
    int y=find(sd,root,0);
    return x+y;
    }
    else if(s>root->data&&sd>root->data)
    {
return search(s,sd,root->right);
    }
    else
    {

return search(s,sd,root->left);
    }

}
node *bst(node *root, int i)
{
    node *temp = insertnode(i);
    if (root == NULL)
    {
        return temp;
    }
    if (i > root->data)
    {
        root->right = bst(root->right, i);
    }
    else
    {
        root->left = bst(root->left, i);
    }
    return root;
}


void inorder(node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

int main()
{

    node *root = NULL;
    int n;
    cin >> n;
    root = bst(root, n);
    for (int i = 0; i < n; i++)
    {
        int k;
        cin >> k;
        root = bst(root, k);
    }

   inorder(root);
   cout<<endl;
   int s,sd;
   cin>>s>>sd;
   int u=search(s,sd,root);
cout<<u<<"\n";
}