#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b)
{
    if(a==0)
    {
        return b;
    }
    if(b==0)
    {
        return a;
    }
    return gcd(b,a%b);
}

int findgcd(int arr[],int n)
{
    int result=arr[0];
    for(int i=1;i<n;i++)
    {
        result=gcd(arr[i],ans);
        if(result==1)
        {
            return 1;
        }
    }

    return result;
}

int lcm(int arr[],int n)
{
    int ans=arr[0];
    for(int i=1;i<n;i++)
    {
        ans=(((arr[i]*ans))/(gcd(arr[i],ans)));
    }

    return ans;
}


int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int m,n;
        con>>m>>n;
       int a[m];
       int b[n];
        for(int i=0;i<m;i++)
        {
            cin>>a[i];
        }
        for(int i=0;i<n;i++)
        {
            cin>>b[i];

        }
        int lcmofarraya=lcm(a,m);
        int gcdofarrayb=findgcd(b,n);
        int count=0;
        for(int i=lcmofarraya;i<=gcdofarrayb;i++){
            if((gcdofarrayb%i)==0)
            {
                count++;
            }
        }
        cout<<count<<endl;


    }
}