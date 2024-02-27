class Solution:
  def dominantIndex(self, nums: [int]) -> int:
    biggest_number = max(nums)
    biggest_index = nums.index(biggest_number)
    for i in range(len(nums)):
      if i != biggest_index and 2*nums[i] > biggest_number:
        return -1
    return biggest_index
  
solution = Solution()
result = solution.dominantIndex([2, 7, 1, 19, 18, 3])
print(result)
