class Solution:
  def numberOfEmployeesWhoMetTarget(self, hours: [int], target: int) -> int:
    count = 0
    for i in hours:
      if i >= target:
        count += 1
    return count