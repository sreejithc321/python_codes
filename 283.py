
class Solution:

    def move_zeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        indx = 0
        for item in nums:
            if item != 0:
                nums[indx] = item
                indx = indx + 1

        for indx in range(indx, len(nums)):
            nums[indx] = 0

        return nums


def test():
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    output = [1, 3, 12, 0, 0]
    result = solution.move_zeroes(nums)
    print(result == output)


if __name__ == '__main__':
    test()
