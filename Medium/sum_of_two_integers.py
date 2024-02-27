class Solution:
  def getSum(self, a: int, b: int) -> int:
    new_list = [a,b]
    sum_of_elements = sum(new_list)
    return sum_of_elements

solution = Solution()
result = solution.getSum(1,5)
print(result)

