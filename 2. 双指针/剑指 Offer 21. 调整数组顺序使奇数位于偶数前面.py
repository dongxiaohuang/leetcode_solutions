class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array or len(array) == 1:
            return array
        i = 0
        for j in range(len(array)):
            if array[j] % 2 != 0:
                k = j
                while k > i:
                    array[k], array[k-1] = array[k-1], array[k]
                    k -= 1
                i += 1
        return array