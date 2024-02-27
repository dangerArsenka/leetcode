class Solution:
  def isPalindrome(self, x: int) -> bool:
    number = x
    reversed_number = 0
    if x < 0:
      return False
    while x != 0:
      digit = x % 10
      reversed_number = reversed_number * 10 + digit
      x //= 10
    if number == reversed_number:
      return True
    else:
      return False
  
solution = Solution()
result = solution.isPalindrome(-121)
print(result)
