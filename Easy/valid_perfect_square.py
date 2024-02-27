class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    c = num ** 0.5
    if c == int(c):
      return True
    else:
      return False


solution = Solution()
result = solution.isPerfectSquare(18)
print(result)