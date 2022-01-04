from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    while l != r:
        currentSum = nums[l] + nums[r]
        if target < currentSum:
            r -= 1
        elif target > currentSum:
            l += 1
        elif currentSum == target:
            return [l+1, r+1]

    return []


numList: List[int] = [2, 7, 11, 15]
# numList: List[int] = [2, 3, 4]
target: int = 9
res = twoSum(numList, target)
print(res)