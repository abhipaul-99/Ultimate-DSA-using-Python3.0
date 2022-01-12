import sys
class Solution:
    def closestToZero (self,arr, n):
        # your code here
        arr.sort()
        ans=sys.maxsize
        i=0
        j=n-1
        while(i<j):
           sumi=arr[i]+arr[j]
           if abs(ans)>abs(sumi):
               ans=sumi
           if abs(ans)==abs(sumi):
               ans=max(ans,sumi)
           if sumi<0:
               i+=1
                       
           else:
               j-=1
        return ans
