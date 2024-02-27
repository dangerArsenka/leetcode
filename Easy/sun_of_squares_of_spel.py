class Solution:
  def sumOfSquares(self, nums: [int]) -> int:
    sum_of_elements = 0
    n = len(nums)
    for i in range(1, n+1):
      if n % i == 0:
        sum_of_elements += nums[i-1]**2
    return sum_of_elements

solution = Solution()
result = solution.sumOfSquares([2,7,1,19,18,3])
print(result)
