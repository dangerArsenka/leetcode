class Solution:
  def findDisappearedNumbers(self, nums: [int]) -> [int]:
    new_list = []
    n = max(nums)
    for i in range(1, n + 1):
      if i not in nums:
        new_list.append(i)
                
    return new_list   

solution = Solution()
result = solution.findDisappearedNumbers([1,1])
print(result)