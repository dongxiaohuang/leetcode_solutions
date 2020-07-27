"""
# BCR
Runtime: O(n)
Spacetime: O(1)

# Brute force soultion
Create z subsets of nums, where z is len(nums) / k
Sort z
calcuate median
Runtime: O(n * k * log k) -- calling merge sort on each subset in z
Spacetime: O(z), -- where z is len(nums) / k

# Two heap apporach
create a max heap and min heap to effecintly model the middle of the array so its easy to calculat the median.
use a sliding window of size k, to iterate through nums and populate the heaps
calcuate the median when heaps equal size k 
slide the window, remove the value that is no longer included, add the new value
repeat

Runtime: O( n * k )
Spacetime: O(k)

"""
import heapq
from heapq import * 

class Solution:
    
    @staticmethod
    def calculate_median(max_heap: List[int], min_heap: List[int]) -> float:
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        return min_heap[0]
    
    @staticmethod
    def add_to_heaps(max_heap: List[int], min_heap: List[int], num) -> None:
        heappush(max_heap, -heappushpop(min_heap, num))
        
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))
    
    @staticmethod
    def remove_from_heap(heap: List[int], num) -> None:
        index = heap.index(num)
        # delete in O(1)
        # replace the value we want to remove with the last value
        heap[index] = heap[-1]
        del heap[-1]
        
        # Restore heap property thoughout the tree
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)
            
    def remove_from_heaps(self, max_heap: List[int], min_heap: List[int], num) -> None:
        if min_heap[0] <= num:
            self.remove_from_heap(min_heap, num)
            return
        self.remove_from_heap(max_heap, -num)
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap: List[int] = []
        min_heap: List[int] = []
        result: List[int] = []
        size_of_k = k - 1

        for i in range(size_of_k):
            self.add_to_heaps(max_heap, min_heap, nums[i])
        
        for i in range(size_of_k, len(nums)):
            self.add_to_heaps(max_heap, min_heap, nums[i])
            median = self.calculate_median(max_heap, min_heap)
            result.append(median)
            self.remove_from_heaps(max_heap, min_heap, nums[i - size_of_k ])
        
        return result