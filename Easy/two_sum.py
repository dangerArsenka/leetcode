# class Solution:
#     def twoSum(self, nums: [int], target: int) -> [int]:
#         index_list =[]
#         for num in range(len(nums)):
#             next_num = target - num
#             if next_num in nums:
#                 index_list.append(nums.index(num))
#                 index_list.append(nums.index(next_num))
#             else:
#                 continue
        
#         return index_list

# solution = Solution()
# result = solution.twoSum([3,3],6)
# print(result)

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        index_list =[]
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in nums[i+1:]:
                complement_index = nums.index(complement,i+1)
                index_list.append(i)
                index_list.append(complement_index)
                break
        
        return index_list

solution = Solution()
result = solution.twoSum([3,3,4],7)
print(result)
                
