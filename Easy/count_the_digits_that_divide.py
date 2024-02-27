class Solution:
  def countDigits(self, num: int) -> int:
    count = 0
    all_digits = []
    x = str(num)
    for digit in x:
      all_digits.append(int(digit))
    for element in all_digits:
      if num % element == 0:
        count += 1
    return count

solution = Solution()
result = solution.countDigits(1248)
print(result)
    
    