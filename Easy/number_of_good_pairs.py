class Solution:
  def numIdenticalPairs(self, nums: [int]) -> int:
    count = 0
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i] == nums[j] and i < j:
          count += 1
    return count

solution = Solution()
result = solution.numIdenticalPairs([2, 7, 1, 19, 18, 3])
print(result)
