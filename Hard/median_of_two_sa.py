class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
      middle_index = 0
      middle_element = 0
      new_list = []
      new_list = nums1 + nums2
      new_list.sort()
      if len(new_list) % 2 == 1:
        middle_index = len(new_list)//2
        middle_element = new_list[middle_index]
        return middle_element
      if len(new_list) % 2 == 0:
        middle_index = len(new_list) // 2
        first_half = new_list[:middle_index]
        second_half = new_list[middle_index:]
        middle_element = (first_half[-1] + second_half[0])/2
        return middle_element
         
solution = Solution()
result = solution.findMedianSortedArrays([1,4],[2,3,6,9])
print(result)

