class Solution:
  def getConcatenation(self, nums: [int]) -> [int]:
    ans = []
    ans += nums
    for i in range(len(nums)):
      ans.append(nums[i])
    return ans

solution = Solution()
result = solution.getConcatenation([1,2,1])
print(result)