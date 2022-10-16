#include <bits/stdc++.h>
using namespace std;

int main()

{

  ifstream fin("student0.txt", ios::in);

  ofstream fout("output.txt", ios::out);
  int testcases;
  fin >> testcases;
  for (int i = 1; i <= testcases; i++)
  {
    int n, m;
    fin >> n >> m;

    vector<int> v,gh;

    for (int i = 0; i < n; i++)

    {
      int r;
      fin >> r;

      v.push_back(r);
    }
    for(int j=0;j<n;j++)
    {
      int r;
      fin>>r;
      gh.push_back(r);
    }
    int flag=0;
    if(m==0)
    {
      if(v!=gh)
      {
        flag=1;
      }
    }
    else{
    for(int i=0;i<n;i++)
    {
    vector<int>::iterator it;
     it= find(v.begin(),v.end(),gh[i]);
    //  cout<<gh[i]<<" "<<v[(it-v.begin()+1)%n]<<"  "<<gh[(i+1)%n]<<"\n";
     if(v[(it-v.begin()+1)%n]!=gh[(i+1)%n])
     {
      flag=1;
break;
     }
      
    }
    }
    if(flag==0)
    {
      fout<<"Case #"<<i<<":"<<" YES"<<"\n";
    }
    else       fout<<"Case #"<<i<<":"<<" NO"<<"\n";

  }
}