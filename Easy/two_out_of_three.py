class Solution:
  def twoOutOfThree(self, nums1: [int], nums2: [int], nums3: [int]) -> [int]:
    new_list = []
    for i in nums1:
      for j in nums2:
        for k in nums3:
          if i == j:
            new_list.append(i)
          if j == k:
            new_list.append(j)
          if i == k:
            new_list.append(k)
    x = set(new_list)
    y = list(x)
    return y

solution = Solution()
result = solution.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])
print(result)
