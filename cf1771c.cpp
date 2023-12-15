#pragma GCC optimize(3)
// #include<bits/stdc++.h>
// #include<stdio.h>
#define endl "\n"
using namespace std;
typedef long long ll;
const int mod=1e9+7;
const int N=4e4+10;

int t,n;
bool p[N];
int prime[N],a[3*N];
int ind=0;
void prime_2()
{
    for(int i=2;i<=4e4;i++)
    { 
        if(!p[i]) prime[++ind]=i;
        for(int j=1;j<=ind;j++)
        {
            if(i*prime[j]>4e4) break;
            p[i*prime[j]]=true;
            if(i%prime[j]==0) break;
        }
    }
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	prime_2();
	while(t--)
	{
		cin>>n;
		for(int i=1;i<=n;i++)
		{
			cin>>a[i];
		}
		map<int,bool> mp;
		bool f=0;
		for(int i=1;i<=n;i++)
		{
			if(a[i]==1)
				continue;
			for(int j=1;j<=ind;j++)
			{
				if(1ll*prime[j]*prime[j]>a[i])
					break;
				if(a[i]%prime[j]==0)
				{
					if(mp[prime[j]]==1)
					{
						f=1;
						break;
					}
					mp[prime[j]]=1;
					while(a[i]%prime[j]==0)
						a[i]/=prime[j];
				}
			}
			if(a[i]>1)
				if(mp[a[i]]==1)
					f=1;
			mp[a[i]]=1;
			if(f)
				break;			
		}
		if(f)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
