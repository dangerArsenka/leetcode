class Solution:
  def convertTemperature(self, celsius: float) -> [float]:
    ans = []
    kelvin = round(celsius + 273.15,5)
    fahrenheit = round(celsius * 1.80 + 32.00,5)
    ans.append(kelvin)
    ans.append(fahrenheit)
    return ans

solution = Solution()
result = solution.convertTemperature(36.509405)
print(result)
    