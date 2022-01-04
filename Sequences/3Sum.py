from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    res = []
    nums.sort()
    for currIdx in range(len(nums) - 2):
        # If this value is the same as the previous, skip to prevent duplicates
        if currIdx > 0 and nums[currIdx] == nums[currIdx - 1]:
            continue

        l, r = currIdx + 1, len(nums) - 1
        while l != r:
            currentSum = nums[currIdx] + nums[l] + nums[r]
            if currentSum > 0:
                r -= 1
            elif currentSum < 0:
                l += 1
            else:
                res.append([nums[currIdx], nums[l], nums[r]])

                # update the left pointer
                l += 1

                # If the left pointer is pointing at the same value as the previous, skip.
                # This prevents duplicates in our 2 sum.
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
