class Solution:
  def superPow(self, a: int, b: [int]) -> int:
    for i in range(len(b)):
      if len(b) <= 1:
        return a**b[i]
      if len(b) > 1:
        c = int(''.join(map(str, b)))
        return a**c

solution = Solution()
result = solution.superPow(2,[1,0])
print(result)