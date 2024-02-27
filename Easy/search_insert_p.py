class Solution:
  def searchInsert(self, nums: [int], target: int) -> int:
    nums.sort()
    for element in nums:
      if element == target:
        return nums.index(element)
      if element != target:
        nums.append(target)
        nums.sort()
        return nums.index(target)

solution = Solution()
result = solution.searchInsert([2,3,4,5,0,1],6)
print(result)

[0,1,2,3,4,5,7]