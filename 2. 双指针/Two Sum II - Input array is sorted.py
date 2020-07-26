class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

         start = 0
          end = len(numbers)-1
           while start < end:
                _sum = numbers[start] + numbers[end]
                if _sum == target:
                    res = [start+1, end+1]
                    start += 1
                    end -= 1
                elif _sum < target:
                    start += 1
                else:
                    end -= 1
            return res
