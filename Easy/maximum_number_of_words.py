class Solution:
  def mostWordsFound(self, sentences: [str]) -> int:
    new_list = []
    for i in range(len(sentences)):
      x = sentences[i].split()
      c = len(x)
      new_list.append(c)
    return max(new_list)

solution = Solution()
result = solution.mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(result)
