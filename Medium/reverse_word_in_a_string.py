class Solution:
  def reverseWords(self, s: str) -> str:
    s = s.split()
    reversed_words = s[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string

    
      
      

solution = Solution()
result = solution.reverseWords(s = "the sky is blue")
print(result)