class Solution:
  def arrangeCoins(self, n: int) -> int:
    i = 1
    while n != 0:
      n = n - i
      i += 1
      if n - i < 0:
        return i-1

solution = Solution()
result = solution.arrangeCoins(11)
print(result)