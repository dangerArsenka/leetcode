class Solution:
  def moveZeroes(self, nums: [int]) -> None:
    nums.sort
    if nums == [0]:
      return [0]
    for element in nums:
      if element == 0:
        nums.remove(element)
        nums.append(element)
    return nums

solution = Solution()
result = solution.moveZeroes([1,2,3,0,0,10,15,0])
print(result)
