'''
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

思路：先对列表进行排序，再用双指针
'''


nums = [-1, 0, 1, 2, -1, -4]
# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]


def threeSum(nums):
    count = len(nums)
    res = []
    nums.sort()
    if count < 3:
        return res
    for i in range(count):
        if nums[i] > 0:
            return res
        if i-1 >= 0 and nums[i] == nums[i-1]:
            continue
        L = i + 1
        R = count - 1
        while R > L:
            if nums[L] + nums[i] + nums[R] == 0:
                res.append([nums[L], nums[i], nums[R]])
                L += 1
                R -= 1
                while L < count and L - 1 > 0 and nums[L] == nums[L - 1]:
                    L += 1
                while R > 0 and R + 1 < count and nums[R] == nums[R + 1]:
                    R -= 1
            elif nums[L] + nums[i] + nums[R] < 0:
                L += 1
            else:
                R -= 1

    return res


print(threeSum(nums))