class Solution:
  def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
    time = arrivalTime + delayedTime
    if time > 24:
      return time-24
    if time == 24:
      return 0
    else:
      return time