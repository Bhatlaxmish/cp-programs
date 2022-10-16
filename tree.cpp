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
void putinarray(node *root, int arr[])
{
    int i = 0;
    if (root != NULL)
    {
        putinarray(root->left, arr);
        arr[i++] = root->data;
        putinarray(root->right, arr);
    }
}
void mergearray(int arr1[], int arr2[], int arr3[], int n, int m)
{
    int i = 0, j = 0, k = 0;
    while (i < n && j < m)
    {
        if (arr1[i] < arr2[j])
        {
            arr3[k] = arr1[i];
            i++;
            k++;
        }
        else
        {
            arr3[k] = arr2[j];
            j++;
            k++;
        }
    }

    while (i < n)
    {
        arr3[k] = arr1[i];
        k++;
        i++;
    }
    while (j < m)
    {
        arr3[k] = arr2[j];
        k++;
        j++;
    }
}

node *createbst(int arr[], int start, int end)
{

    if (start > end)
        return NULL;

    int mid = (start + end) / 2;
    node *root = insertnode(arr[mid]);

    root->left = createbst(arr, start, mid - 1);

    root->right = createbst(arr, mid + 1, end);

    return root;
}

void mergetree(node *root, node *root2, int n, int m)
{
    int arr1[n], arr2[m];
    putinarray(root, arr1);
    putinarray(root2, arr2);
    int arr3[m + n];
    mergearray(arr1, arr2, arr3, n, m);
   

    node*root3= createbst(arr3, 0, m + n-1);
    inorder(root3);
  
}

int main()
{

    node *root = NULL;
    node *root2 = NULL;
    int n;
    cin >> n;
    root = bst(root, n);
    for (int i = 0; i < n; i++)
    {
        int k;
        cin >> k;
        root = bst(root, k);
    }

    int m;
    cin >> m;
    root2 = bst(root2, m);
    for (int j = 0; j < m; j++)
    {
        int r;
        cin >> r;
        root2 = bst(root2, r);
    }
    inorder(root);
    cout << endl;
    inorder(root2);

    mergetree(root, root2, n, m);
    
}