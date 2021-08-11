'''

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

'''


nums = [0,2,1,-3]
target = 1


def threeSumClosest(nums, target):
    count = len(nums)
    res = None
    dist = 0
    if count < 3:
        return res
    nums.sort()
    for i in range(count):
        L = i + 1
        R = count - 1
        while R > L:
            temp_res = nums[L] + nums[i] + nums[R]
            temp_dist = abs(target - temp_res)
            if res is None or temp_dist < dist:
                res = temp_res
                dist = temp_dist
            if target - temp_res == 0:
                return res
            elif target - temp_res > 0:
                while L<R and nums[L] == nums[L+1]:
                    L += 1
                L += 1
            else:
                while L<R and nums[R] == nums[R-1]:
                    R -= 1
                R -= 1
    return res


print(threeSumClosest(nums, target))