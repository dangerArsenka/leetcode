class Solution:
  def commonFactors(self, a: int, b: int) -> int:
    count = 0 
    list_a = []
    list_b = []
    for digit in range(1,a+1):
      if a % digit == 0:
        list_a.append(digit)
    for digit in range(1,b+1):
      if b % digit == 0:
        list_b.append(digit)
    for i in list_a:
      for k in list_b:
        if i == k:
          count += 1
    return count

solution = Solution()
result = solution.commonFactors(12,6)
print(result)
