class Solution:
  def reverse(self, x: int) -> int:
    reversed_number = 0
    is_negative = False
    
    if x < 0:
      is_negative = True
      x *= -1

    while x != 0:
      digit = x % 10
      if reversed_number > (2**31 - 1 - digit) // 10:
        return 0
      reversed_number = reversed_number * 10 + digit
      x //= 10

    if is_negative:
      reversed_number *= -1

    return reversed_number

solution = Solution()
result = solution.reverse(123)
print(result)
