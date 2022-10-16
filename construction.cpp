#include <bits/stdc++.h>
using namespace std;
struct node
{
    int data;
    node *left, *right;
};
node *createroot()
{
    node *temp;
    temp = new node;
    temp->left = temp->right = NULL;
    return temp;
}

node *insertinbinarytree( node *root,int data)
{
    node *temp, *cur, *prev;
    temp =createroot();
    temp->data = data;
    if (root == NULL)
        return temp;
    prev = NULL;
    cur = root;
    while (cur != NULL)
    {
        prev = cur;
        cur = (data <= cur->data) ? cur->left : cur->right;
    }

    if (data < prev->data)
        prev->left = temp;
    else
        prev->right = temp;
    return root;
}

node *insert(node *root, int data)
{
    node *temp = createroot();
    temp->data = data;
    if (root == NULL)
    {
        return temp;
    }
    if (data > root->data)
    {
        root->right = insert(root->right, data);
    }
    else
    {
        root->left = insert(root->left, data);
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
    cout<<"create binary tree"<<"\n";
    node*root=NULL;

    root=insert(root,3);
    insert(root,6);
    insert(root,2);
    insert(root,68);
    insert(root,5);
    insert(root,23);
    insert(root,7);
    inorder(root);
    cout<<endl;
    cout<<root->right->left->data<<"\n";

    // or
    int n;
    cin >> n;
    node *head = NULL;
    int d;
    cin >> d;
    head = insertinbinarytree(head, d);

    for (int i = 0; i < n; i++)
    {

        int data;
        cin >> data;

        head = insertinbinarytree(head, data);
    }
    inorder(head);
}