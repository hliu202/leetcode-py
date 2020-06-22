# https://leetcode-cn.com/problems/pattern-matching-lcci/

from util.common_imports import *

# !但需注意"a"和"b"不能同时表示相同的字符串

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        C = Counter(pattern)

        if not value:
            return len(C.keys()) != 2
        if not pattern:
            return False
        if len(pattern) == 1:
            return True

        nv = len(value)
        target0 = pattern[0]

        def is_single_t(tar):
            nk = C.get(tar)
            if not nk:
                return False

            if nv % nk != 0:
                return False
            p_len = nv // nk
            p_p = value[0:p_len]
            p_end = p_len
            while p_end != nv:
                if value[p_end : p_end + p_len] != p_p:
                    return False
                p_end = p_end + p_len
            return True

        if len(C.keys()) == 1:
            return is_single_t(target0)
        if is_single_t("a") or is_single_t("b"):
            return True

        target1 = "a" if target0 == "b" else "b"
        for t0_len in range(1, nv - 1):
            p_t1 = ""
            t0_n = C.get(target0)
            t1_n = C.get(target1)

            if t0_n * t0_len >= nv:
                return False
            t1_sum = nv - t0_n * t0_len
            if t1_sum % t1_n != 0:
                continue

            t1_len = t1_sum // t1_n

            p_end = t0_len
            p_t0 = value[0:p_end]
            p_i = 1

            match = True
            while p_i < len(pattern):
                cur_t = pattern[p_i]
                p_i += 1
                if cur_t == target0:
                    if value[p_end : p_end + t0_len] != p_t0:
                        match = False
                        break

                    p_end += t0_len
                else:
                    if not p_t1:
                        p_t1 = value[p_end : p_end + t1_len]
                        if p_t1 == p_t0:
                            match = False
                            break

                        p_end += t1_len
                        continue
                    if value[p_end : p_end + t1_len] != p_t1:
                        match = False
                        break
                    p_end += t1_len

            if match:
                return True

        return False


print(Solution().patternMatching(pattern="abba", value="dogcatcatdog"))
print(Solution().patternMatching(pattern="abba", value="dogcatcatfish"))
print(Solution().patternMatching(pattern="aaaa", value="dogcatcatdog"))
print(Solution().patternMatching(pattern="abba", value="dogdogdogdog"))
print(Solution().patternMatching(pattern="ab", value=""))
