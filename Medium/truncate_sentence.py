class Solution:
  def truncateSentence(self, s: str, k: int) -> str:
    x = s.split()
    while len(x) != k:
      x.pop(-1)
    c = ' '.join(x)
    return c


solution = Solution()
result = solution.truncateSentence("Hello how are you Contestant",2)
print(result)    