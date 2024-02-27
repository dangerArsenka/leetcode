class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    product_of_digits = 1
    new_list = []
    for digit in str(n):
      new_list.append(int(digit))
    for i in new_list:
      product_of_digits *= i
      sum_of_digits = sum(new_list)
    return product_of_digits - sum_of_digits

solution = Solution()
result = solution.subtractProductAndSum(234)
print(result)