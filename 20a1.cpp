
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
// int dp[100000]={};

bool compi(pair<int,int>v2,pair<int,int>p3)
{
    return v2.second<p3.second;
}
int main()
{
    
   int t;
   cin>>t;
   while(t--)
   {
    int n;
    cin>>n;
    vector<pair<int, string>> v;
    for(int i=0;i<2*n-2;i++)
    {
string s;
cin>>s;
v.push_back({s.size(),s});
    }
    sort(v.rbegin(),v.rend());
    // for(auto x:v)
    // {
    //     cout<<x.first<<" "<<x.second<<"\n";
    // }
    string fr=v[0].second;
    string fe=v[1].second;
    int gh = 0;

    for(int i=0;i<fe.size();i++)
    {
        if(fe[i]==fr[0])
        {
            break;
        }
    }

   
    






   } 
    
    
    
  

   
}
