class Solution:
  def differenceOfSum(self, nums: [int]) -> int:
    digit_list = []
    element_sum = sum(nums)
    digit_sum = 0
    for num in nums:
      if num >= 10:
        x = str(num)
        for digit in x:
          digit_list.append(int(digit))
      else:
        digit_list.append(num)
    digit_sum = sum(digit_list)
    return abs(element_sum - digit_sum)
    

solution = Solution()
result = solution.differenceOfSum([1,15,6,3])
print(result)
    