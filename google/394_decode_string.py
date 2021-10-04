# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                sub_str = []
                num = []

                while (p := stack.pop()) != "[":
                    sub_str.append(p)

                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                sub_str = sub_str[::-1]
                num = int("".join(num[::-1]))

                for i in range(num):
                    stack.extend(sub_str)
            else:
                stack.append(c)

        return "".join(stack)

    def decodeStringFailedOnNested(self, s: str) -> str:

        left_idx = []
        right_idx = []

        for i, c in enumerate(s):
            if c == "[":
                left_idx.append(i)
            elif c == "]":
                right_idx.append(i)


        subs = []
        for i, (l, r) in enumerate(zip(left_idx, right_idx)):

            num = s[l-1]
            sub_s = s[l+1: r]
            if i == 0:
                prefix = s[0: l-1]
            else:
                last_r = right_idx[i-1]
                prefix = s[last_r+1:l-1]

            subs.append(prefix)
            subs.append(sub_s * int(num))

        if (final_r := right_idx[-1]) != len(s):
            subs.append(s[final_r + 1:])
        return "".join(subs)