class Solution:
  def countSegments(self, s: str) -> int:
    new_list = s.split()
    count = len(new_list)
    return count

    

solution = Solution()
result = solution.countSegments("hello MY NAME IS ARSEN")
print(result)