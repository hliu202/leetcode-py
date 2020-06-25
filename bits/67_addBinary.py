# https://leetcode-cn.com/problems/add-binary/

# recursive
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return b if not a else a

        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        if a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1], b[:-1]) + "0"
        return self.addBinary(a[:-1], b[:-1]) + "1"


print(Solution().addBinary(a="1010", b="1011"))
print(Solution().addBinary(a="11", b="1"))

# 这题完全可以用来练习一下递归的写法。我们按照位数来做递归。
# 每位数字相加之后一共有三种情况：
# 1.都是0，不进位
# 2.有一个是1，不进位
# 3.要进位
# 进位无非就是在上一位加减时多一个1而已，举例来说：
# a,b = '1100','110'
# addBinary('1100' , '110') -> addBinary('110','11') + '0'
# ->addBinary('11','1')+'10' -> addBinary(addBinary('1',''),'1') + '010'
# ->addBinary('1','1')+'010' -> addBinary(addBinary('',''),'1') + '0010'
# ->'10010'

# 作者：rysander
# 链接：https://leetcode-cn.com/problems/add-binary/solution/di-gui-fang-fa-qiu-jie-by-rysander/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
