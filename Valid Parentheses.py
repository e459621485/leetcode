'''

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


s = "()"


def isValid(s):
    dict = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    l = []
    for i in s:
        if i in dict.keys():
            l.append(i)
        elif l and i == dict[l.pop()]:
            continue
        else:
            return False
    if l:
        return False
    return True


print(isValid(s))


