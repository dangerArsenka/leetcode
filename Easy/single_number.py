class Solution:
    def singleNumber(self, nums: [int]) -> int:
        nums.sort()  # Сортируем массив, чтобы одинаковые числа шли рядом
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        for i in range(0, n, 2):
            if i + 1 >= n or nums[i] != nums[i + 1]:
                return nums[i]
        
solution = Solution()
result = solution.singleNumber([1])
print(result)

            