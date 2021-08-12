'''

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。



示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11


def fourSum(nums, target):
    res = []
    count = len(nums)
    nums.sort()
    if count < 4:
        return res
    i = 0
    while i < count:
        j = i + 1
        while j < count:
            # if nums[i] + nums[j] > target:
            #     break
            L = j + 1
            R = count - 1
            while R > L:
                if nums[i] + nums[j] + nums[L] + nums[R] == target:
                    res.append([nums[i], nums[j], nums[L], nums[R] ])
                    while R > L and nums[L + 1] == nums[L]:
                        L += 1
                    while R > L and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[j] + nums[L] + nums[R] > target:
                    R -= 1
                else:
                    L += 1
            while j + 1 < count and nums[j] == nums[j + 1]:
                j += 1
            j += 1
        while i + 1 < count and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return res


print(fourSum(nums, target))