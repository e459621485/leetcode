'''

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

n = 3

import copy
def generateParenthesis(n):
    res = []
    if n == 0:
        return res
    if n == 1:
        res.append("()")
        return res
    for i in generateParenthesis(n - 1):
        for j in range(len(i) + 1):
            # temp = copy.deepcopy(i)
            temp = list(i)
            temp.insert(j, "()")
            temp = "".join(temp)
            if temp not in res:
                res.append(temp)
    return res

print(generateParenthesis(n))
