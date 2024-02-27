class Solution:
  def search(self, nums: [int], target: int) -> bool:
    if target in nums:
      return True
    else:
      return False

solution = Solution()
result = solution.search([2,3,4,5,0,1],6)
print(result)