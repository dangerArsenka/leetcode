# class Solution:
#     def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
#         distance = 0
#         if mainTank < 5:
#             distance = mainTank*10
#         elif mainTank == 5 and additionalTank >= 1:
#             distance = mainTank*10 + 10
#         elif mainTank > 5 and additionalTank >= 1:
#             distance += 6 * 10
#             remaining_main = mainTank - 5
#             if remaining_main < 5:
#                 distance += remaining_main*10
#         return distance

# solution = Solution()
# result = solution.distanceTraveled(9,2)
# print(result) 

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank > 0:
            distance += mainTank * 10  
            if mainTank >= 5:
                mainTank -= 5 
            elif additionalTank > 0:
                mainTank += 1  
                additionalTank -= 1
            else:
                break 
        return distance

solution = Solution()
result = solution.distanceTraveled(6, 1)
print(result)


