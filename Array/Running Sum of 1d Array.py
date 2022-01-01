def runningSum(nums):
      n = len(nums)
      s = [nums[0]]*n
        
      for i in range(1,n):
          s[i] = s[i-1] + nums[i]
      return s
  
arr = [1,1,1,1,1]

print(runningSum(arr))
