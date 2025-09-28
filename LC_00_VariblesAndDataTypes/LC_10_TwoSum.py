# No need to import List for simple type hints; use built-in list for clarity
from typing import List


class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          for i in range(len(nums)):
               for j in range(i + 1, len(nums)):
                    if(nums[i] + nums[j] == target):
                         return [i, j]
          # Return an empty list if no solution is found
          return []
                    
mySolutionClass = solution()

print(mySolutionClass.twoSum([3,2,4], 6))
        

        
        