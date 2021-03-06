class Solution {
    typedef long long ll;
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n=bloomDay.size(),i,j,l,r,mid,s;
        if((ll)m*k>n)return -1;
        l=0;
        r=1000000000;
        while(l+1<r)
        {
            mid=l+r>>1;
            for(i=j=s=0;i<n;i++)if(bloomDay[i]<=mid)j++;
            else
            {
                s+=j/k;
                j=0;
            }
            s+=j/k;
            if(s>=m)r=mid;
            else l=mid;
        }
        return r;
    }
};