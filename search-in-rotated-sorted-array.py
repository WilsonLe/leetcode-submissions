# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums, target: int) -> int:
        # find rotation index
        start, rotationIndex = 0, 0
        while rotationIndex != len(nums) - 1 and nums[rotationIndex] < nums[rotationIndex+1]:
            if nums[rotationIndex] >= nums[start]:
                start = rotationIndex
                rotationIndex = (len(nums) + start) // 2
            else:
                rotationIndex = (rotationIndex + start) // 2

        # decide whether target in left or right partition
        if rotationIndex + 1 > len(nums) - 1:
            # target in whole array, array was not rotated
            i, j = 0, len(nums) - 1
        elif target < nums[0]:
            # target is in right partition
            i, j = rotationIndex + 1, len(nums) - 1
        elif target >= nums[0] and target <= nums[rotationIndex]:
            # target is in left partition
            i, j = 0, rotationIndex
        elif target >= nums[rotationIndex+1] and target < nums[-1]:
            # target is in right partition
            i, j = rotationIndex + 1, len(nums) - 1
        else:
            # target does not exist
            return -1

        # run binary search on the partition
        mid = (i + j) // 2
        while i < j and nums[mid] != target:
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
            mid = (i + j) // 2

        if nums[mid] != target and i >= j:
            return -1
        return mid

    def search2(self, nums, target: int) -> int:
        # attempt 2, this time iterating through array only once
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[start]:
                if target >= nums[start] and target <= nums[mid-1]:
                    end = mid - 1
                    continue
                else:
                    start = mid + 1
                    continue
            else:
                if mid >= len(nums) - 1:
                    return -1
                if target >= nums[mid+1] and target <= nums[end]:
                    start = mid + 1
                    continue
                else:
                    end = mid - 1
                    continue
        return -1


assert (Solution().search([3, 5, 1], 3) == 0)
assert (Solution().search([3, 5, 1], 1) == 2)
assert (Solution().search([3, 1], 3) == 0)
assert (Solution().search([3, 1], 1) == 1)
assert (Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 1) == 5)
assert (Solution().search([1], 1) == 0)


assert (Solution().search2([3, 4, 5, 1, 2], 4) == 1)
assert (Solution().search2([4, 5, 6, 7, 0, 1, 2], 3) == -1)
assert (Solution().search2([3, 5, 1], 3) == 0)
assert (Solution().search2([3, 5, 1], 1) == 2)
assert (Solution().search2([3, 1], 3) == 0)
assert (Solution().search2([3, 1], 1) == 1)
assert (Solution().search2([4, 5, 6, 7, 8, 1, 2, 3], 1) == 5)
assert (Solution().search2([1], 1) == 0)
