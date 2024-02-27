class Solution:
  def finalValueAfterOperations(self, operations: [str]) -> int:
    X = 0
    for i in range(len(operations)):
      if operations[i] == '++X' or operations[i] == 'X++':
        X += 1
      if operations[i] == '--X' or operations[i] == 'X--':
        X -= 1
    return X

solution = Solution()
result = solution.finalValueAfterOperations(["++X","X++","X++"])
print(result)
