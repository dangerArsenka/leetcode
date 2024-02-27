class Solution:
  def findGCD(self, nums: [int]) -> int:
    min_list = []
    max_list = []
    same_list = []
    min_element = min(nums)
    max_element = max(nums)
    for i in range(1, min_element+1):
      if min_element % i == 0:
        min_list.append(i)
    for i in range(1, max_element+1):
      if max_element % i == 0:
        max_list.append(i)
    for i in min_list:
      for k in max_list:
        if i == k:
          same_list.append(i)
    return max(same_list)

solution = Solution()
result = solution.findGCD([18, 21, 20, 22, 122, 25])
print(result)



