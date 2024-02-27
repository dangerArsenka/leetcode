class Solution:
  def findKthLargest(self, nums: [int], k: int) -> int:
    nums.sort()
    nums.reverse()
    return nums[k-1]

solution = Solution()
result = solution.findKthLargest([5,6,7,8,1,2,3,4],1)
print(result)