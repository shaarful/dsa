from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        result = []
        # base case
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            purms = Solution.permute(nums)
            for purm in purms:
                purm.append(n)
            print(purms)
            result.extend(purms)
            nums.append(n)
        return result


# print('result: ', Solution.permute([1, 2, 3]))

class Permutation:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        result = []
        a = []
        # base case
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            n = nums.pop(0)
            purms = Permutation.permute(nums)
            a.append(purms)
            print('purm: ', purms)
            print('a: ', a)
            # result.extend(purms)
            nums.append(n)
        return result


print('result: ', Permutation.permute([1, 2, 3]))
