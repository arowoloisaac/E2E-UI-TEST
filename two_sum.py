from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            check_sum = numbers[i] + numbers[j]
            if check_sum == target:
                return [i + 1, j + 1]

            elif check_sum < target:
                i += 1

            else:
                j -= 1

        return []


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

s = Solution()
print(s.twoSum(num, target))
