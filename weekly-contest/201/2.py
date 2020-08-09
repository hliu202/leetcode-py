class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k -= 1
        cur = ["0"]
        if k == 0:
            return "0"

        def invert(a):
            for i in range(len(a)):
                a[i] = "1" if a[i] == "0" else "0"
            return a

        def reverse(lx):
            return lx[::-1]

        for _ in range(n - 1):
            ri = reverse(invert(cur.copy()))
            cur.append("1")
            cur.extend(ri)
            if k < len(cur):
                return cur[k]
        return None


# print(Solution().findKthBit(n = 3, k = 1))
print(Solution().findKthBit(n=4, k=11))
print(Solution().findKthBit(n=2, k=3))
print(Solution().findKthBit(n=1, k=1))

