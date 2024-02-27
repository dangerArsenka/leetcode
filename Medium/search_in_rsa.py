class Solution:
  def search(self, nums: [int], target: int) -> int:
    for i in range(len(nums)):
      if target in nums:
        index = nums.index(target)
        return index
      else:
        return -1

solution = Solution()
result = solution.search([5,6,7,8,1,2,3,4],6)
print(result)