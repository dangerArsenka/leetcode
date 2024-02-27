class Solution:
  def buildArray(self, nums: [int]) -> [int]:
    ans = []
    for i in range(len(nums)):
      x = nums[nums[i]]
      ans.append(x)
    return ans


solution = Solution()
result = solution.buildArray([0,2,1,5,3,4])
print(result)