# https://leetcode-cn.com/problems/longest-valid-parentheses/


# 动态规划

# * 1) dp[i] 表示:
# *      以下标 i 字符结尾的最长有效括号的长度
# 2.1) if '()': dp[i] = dp[i-2] + 2
# 2.2) if '?(...))': dp[i] = if s[i - dp[i-1] -1] == '(' : 2 + dp[i-1] + dp[i - dp[i-1] -1-1]
#         ↑     i           if s[i - dp[i-1] -1] == ')' : 0
# !合理利用dp[i-1] if s[i-1] == ')'

public class Solution {
    public int longestValidParentheses(String s) {
        int maxans = 0;
        int dp[] = new int[s.length()];
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                if (s.charAt(i - 1) == '(') {
                    dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
                } else if (i - dp[i - 1] > 0 && s.charAt(i - dp[i - 1] - 1) == '(') {
                    dp[i] = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
                }
                maxans = Math.max(maxans, dp[i]);
            }
        }
        return maxans;
    }
}

# * 栈底元素为：
# *  「最后一个没有被匹配的右括号」  or  -1 if s[0]='(': 不算
# 对于遇到的每个 ( ，我们将它的下标放入栈中
# 对于遇到的每个 ) ，我们先弹出栈顶元素表示匹配了当前右括号，or栈底「不匹配当前右括号，栈底更新」
public class Solution {
    public int longestValidParentheses(String s) {
        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());
                }
            }
        }
        return maxans;
    }
}

