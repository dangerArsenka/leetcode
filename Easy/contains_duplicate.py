class Solution:
  def containsDuplicate(self, nums: [int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
      if nums[i] == nums[i+1]:
        return True
    return False
        
solution = Solution()
result = solution.containsDuplicate([1,2,3,4,5,5])
print(result)