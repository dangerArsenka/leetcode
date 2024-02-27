class Solution:
  def singleNumber(self, nums: [int]) -> [int]:
    new_list = []
    nums.sort()
    for i in range(len(nums)):
      if nums.count(nums[i]) == 1:
        new_list.append(nums[i])
    return new_list

solution = Solution()
result = solution.singleNumber([1,2,3,2,3,5])
print(result)