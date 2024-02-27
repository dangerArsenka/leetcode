class Solution:
  def runningSum(self, nums: [int]) -> [int]:
    new_list = []
    element = 0
    for i in nums:
      element += i
      new_list.append(element)
    return new_list

solution = Solution()
result = solution.runningSum([3,1,2,10,1])
print(result)