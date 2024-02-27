class Solution:
  def findPeakElement(self, nums: [int]) -> int:
    for i in range(len(nums)):
      c = max(nums)
      return nums.index(c)

solution = Solution()
result = solution.findPeakElement([2, 7, 1, 19, 18, 3])
print(result)
