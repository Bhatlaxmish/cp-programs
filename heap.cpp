#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void swap(int *a,int *b)

{
    int *temp;
    temp=a;
    a=b;
    b=temp;
}
int parent(int i)
{
    return (i-1)/2;
}
int findleft(int i)
{
    return 2*i-1;
    
    }

    int findright(int i)
    {
        return 2*i+1;
            }
void heapinsert(int r,int arr[],int heapsize,int n)
{
    if(heapsize==n)
    {
        cout<<"overflow";
        return;
    }
    heapsize++;
    arr[heapsize-1]=r;
    int i=heapsize-1;

  while(i>=0 && arr[parent(i)]>arr[i])
    {
swap(&arr[i],&arr[parent(i)]);
i=parent(i);
    }

}
void decreasekey(int i,int arr[],int newvalue)
{
arr[i]=newvalue;
while(i>0&&arr[parent(i)]>arr[i])
{
    swap(&arr[i],&arr[parent(i)]);
    i=parent(i);
}
}

void minheapify(int i,int heapsize,int arr[])
{
    int leftchildindex=findleft(i);
    int rightchildindex=findright(i);
    int smallest=i;
    if(leftchildindex<heapsize&&arr[leftchildindex]<arr[i])
    {
        smallest=leftchildindex;
    }
    if(rightchildindex<heapsize&&arr[rightchildindex]<arr[smallest])
    {
        smallest=rightchildindex;
    }
    if(smallest!=i)
    {
        swap(arr[i],arr[smallest]);
        minheapify(smallest,heapsize,arr);
    }
}
int  minimumelement(int arr[],int heapsize){
    if(heapsize<=0)
    {
        return INT_MAX;
    }
    if(heapsize==1)
    {
        heapsize--;
        return arr[0];
    }
    int minimumele=arr[0];
    arr[0]=arr[heapsize-1];
    heapsize--;
    minheapify(0,heapsize,arr);
    return minimumele;


}


int main()
{
int n;
cin>>n;
int arr[n];
int heapsize=0;
for(int i=0;i<n;i++)
{
    int r;
   cin>>r;
   heapinsert(r,arr,heapsize,n);

}
for(int i=0;i<n;i++)
{
    cout<<arr[i]<<" ";
}

}