
# n = 3, 1+2+3 = (1+3) * (3/2) + 2
# n = 4, 1+2+3+4 = (1+4) * (4/2)

class Solution:
    def sumNums(self, n: int) -> int:
        return n > 0 and (n + self.sumNums(n-1))


print(Solution().sumNums(6))


# java implementation

class Solution {
    public int sumNums(int n) {
        boolean x = n > 1 && (n += sumNums(n - 1)) > 0;
        return n;
    }
}
class Solution {
    int res = 0;
    public int sumNums(int n) {
        boolean x = n > 1 && sumNums(n - 1) > 0;
        res += n;
        return res;
    }
}
