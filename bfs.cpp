
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007

#define powe pow(2, 31)
ll araisetobwithmod(ll base, ll exp)
{
    ll result = 1;
    for (;;)
    {
        if (exp & 1)
            result = (result * base) % mod;
        ;
        exp >>= 1;
        if (!exp)
            break;
        base = (base * base) % mod;
    }

    return result;
}
ll factorialwithmod(ll n)
{
    if (n >= mod)
        return 0;

    ll result = 1;
    for (int i = 1; i <= n; i++)
        result = (result * i) % mod;

    return result;
}
bool isprimeornot(ll n)
{
    if (n == 1)
    {
        return false;
    }
    ll i = 2;
    while (i * i <= n)
    {
        if (n % i == 0)
        {
            return false;
        }
        i += 1;
    }
    return true;
}

ll araisetob(ll a, ll b)
{
    ll ans = 1;
    while (b > 0)
    {
        if (b & 1)
        {
            ans = (ans * 1LL * a);
        }
        a = (a * 1LL * a);
        b >>= 1;
    }
    return ans;
}
bool isperfectsquareornot(ll x)
{
    if (sqrt(x) * sqrt(x) == x)
    {
        return true;
    }
    return false;
}
bool ispoweroftwoornot(ll n)
{
    if (n == 0)
        return false;

    return (ceil(log2(n)) == floor(log2(n)));
}
ll factorial(ll n)
{

    return (n == 1 || n == (ll)0) ? (ll)1 : n * factorial(n - 1);
}
ll maximumsubarraysum(vector<int> a, ll size)
{
    ll currmax = -1111111111, until = 0;

    for (ll i = 0; i < size; i++)
    {
        until = until + a[i];
        if (currmax < until)
            currmax = until;

        if (until < 0)
            until = 0;
    }
    return currmax;
}
bool ispalindromeornot(string s, ll n)
{
    ll l = 0;
    ll h = n - 1;
    while (h > l)
    {
        if (s[l++] != s[h--])
        {

            return false;
        }
    }
    return true;
}

ll gcd(ll a, ll b)
{
    if (b > a)
    {
        return gcd(b, a);
    }
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

ll araisetobwithmodeasy(ll a, ll b)
{
    ll res = 1;
    while (b > 0)
    {
        if (b & 1)

            res = (res * a) % mod;
        a = (a * a) % mod;
        b = b >> 1;
    }
    return res;
}

ll ncr(ll n, ll r)
{
    if (r > n || n < 0 || r < 0)
        return 0;
    vector<ll> fact(n + 1);
    vector<ll> ifact(n + 1);
    int i;
    fact[0] = 1;
    for (i = 1; i <= n; i++)
    {
        fact[i] = i * fact[i - 1] % mod;
    }
    i--;
    ifact[i] = araisetobwithmod(fact[i], mod - 2);
    for (i--; i >= 0; i--)
    {
        ifact[i] = ifact[i + 1] * (i + 1) % mod;
    }
    ll val1 = fact[n];
    ll val2 = ifact[n - r];
    ll val3 = ifact[r];
    return (((val1 * val2) % mod) * val3) % mod;
}

ll countnoofdivisors(int n)
{
    ll cnt = 0;
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            cnt++;
            // cout<<i<<" ";
            if (i != (n / i))
            {
                cnt++;
                // cout<<n/i<<" ";
            }
        }
    }
    return cnt;
}
int rotateBinary(int number)
{
    int res = 0;
    while (number > 0)
    {
        res = res << 1;
        res = res | (number & 1);
        number = number >> 1;
    }
    return res;
}

int compi(pair<int, int> v3, pair<int, int> v2)
{
    return v3.second < v2.second;
}

void dfs(list<int> adj[], vector<bool> &visited, int i)
{
    visited[i] = true;
  
    for (auto x : adj[i])
    {

        if (!visited[x])
        {
            dfs( adj, visited,x);
        }
    }
    cout << i << " ";
}

int main()
{

    //    bool ispalindromeornot(string s, ll n)
    //    ll factorial(ll n)
    //    ll factorialwithmod(ll n)
    //    bool ispoweroftwoornot(ll n)
    //    bool isperfectsquareornot(ll x)
    //    bool isprimeornot(ll n)
    //    ll araisetobwithmod(ll base, ll exp)
    //    ll araisetob(ll a, ll b)
    //    bool powof2ornot(ll x)
    //    ll maximumsubarraysum(vector<int>a, ll size)
    //    ll countnoofdivisors(int n)
    //    ll ncr(ll n, ll r)
    //    ll araisetobwithmodeasy(ll a, ll b)
    //    ll gcd(ll a, ll b)
    //    ll countnoofdivisors(int n)
    // float rt= ((float) a/(float) c);
    // pos[s[z]-'a'].push_back(z);
    // to convert string to int use stoi(str)
    // to convert int to string use to_string(int)
    // to convert char to int use int(char)-48
    // int t;
    // cin >> t;
    // while (t--)
    {
    int n,m;
    cin>>n>>m;
    list<int>adj[n+1];
    for(int i=0;i<m;i++)
    {
        int r,s;
        cin>>r>>s;
        adj[r].push_back(s);
        adj[s].push_back(r);
    }
    vector<bool>visited(n+1,false);
   dfs(adj,visited,1);
    int q;
    cin>>q;
    for(int i=0;i<n;i++)
    {
        int r;
        cin>>r;
        if(r==3)
        {
            cout<<1<<"\n";
        }
        else {
            int o,el;
            cin>>o>>el;

        }
    }


}
}
