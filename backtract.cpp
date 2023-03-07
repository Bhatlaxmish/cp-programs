#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        // interhostel
        int n, m;
        cin >> n >> m;
      
        string s;
        long long int mar = 0;
        cin >> s;
        vector<int> v;
        int count = 1;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == s[i + 1])
            {
                count++;
            }
            else
            {
                v.push_back(count);
                count = 1;
            }
        }
        long long sum = 0, sum2 = 0, sum3 = 0;
        vector<long long int> pre1, pre2;
        // for (int i = 0; i < n; i++)
        // {
        //     if (i % 2 == 0)
        //     {
        //         sum += v[i];
        //         pre1.push_back(sum);
        //     }
        //     else
        //     {
        //         sum2 += v[i];
        //         pre2.push_back(sum2);
        //     }
        // }
        for(auto x:v)
        {
            cout<<x<<" ";
        }

        cout<<endl;
        if (s[0] == '1')
        {
            
            int sg = v.size();
            for (int i = 0; i < sg; i += 2)
            {

                int jk = m;
                sum3=0;
                // cout<<"starting from" <<i<<" \n";
                for (int j = i + 1; j < sg && jk > 0; j += 2)
                {
                    jk = jk - v[j];
                    sum3 = sum3 + v[j] + v[j - 1];
                    // cout<<"adding "<<v[j]<<" ";
                }
                if (jk < 0)
                {
                    sum3 += jk;
                }
                else
                {
                    // cout << (i) % v.size() <<" "<<v[(i + 1) % v.size()-1] << "\n";
                    sum3 += v[(i +1) % v.size()-1];
                    for (int k = 0; k < i && jk > 0; k += 2)
                    {
                        jk = jk - v[k];
                        // cout << "adding " << v[k] <<" ";
                        sum3 = sum3 + v[k] + v[k - 1];
                    }
                }
                // cout<<endl;
                mar = max(sum3, mar);
            }
           if(mar>s.size())
           {
            cout<<s.size()<<"\n";
           }
           else {
            cout<<mar<<"\n";
           }
        }

        else
        {

           int sg = v.size();
           for (int i = 1; i < sg; i += 2)
           {

            int jk = m;
            sum3 = 0;
            // cout<<"starting from" <<i<<" \n";
            for (int j = i + 1; j < sg && jk > 0; j += 2)
            {
                    jk = jk - v[j];
                    sum3 = sum3 + v[j] + v[j - 1];
                    // cout<<"adding "<<v[j]<<" ";
            }
            if (jk < 0)
            {
                    sum3 += jk;
            }
            else
            {
                    // cout << (i) % v.size() <<" "<<v[(i + 1) % v.size()-1] << "\n";
                   
                    for (int k = 0; k < i && jk > 0; k += 2)
                    {
                        jk = jk - v[k];
                        // cout << "adding " << v[k] <<" ";
                        sum3 = sum3 + v[k] + v[(k - 1)>0?k-1:0];
                    }
            }
            // cout<<endl;
            mar = max(sum3, mar);
           }
           if (mar > s.size())
           {
            cout << s.size() << "\n";
           }
           else
           {
            cout << mar << "\n";
           }
        }
    }
}




