class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    words  = s.split()
    last_element = words[-1]
    return len(last_element)


solution = Solution()
result = solution.lengthOfLastWord(s = "Hello World")
print(result)
