class Solution:
  def thirdMax(self, nums: [int]) -> int:
    unique_nums = set(nums)
    if len(unique_nums) <3:
      return max(unique_nums)
    unique_nums.remove(max(unique_nums))
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)

solution = Solution()
result = solution.thirdMax([2,1,1])
print(result)
