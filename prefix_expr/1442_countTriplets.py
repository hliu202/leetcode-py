# https://leetcode-cn.com/contest/weekly-contest-188/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
# 因为 a ^ a = 0, a ^ a ^ b = b
# 1: A[i, j) = A[0, i-1] ^ A[0, j-1)
# 2: A[j, k] = A[j, len) ^ A[k+1, len), or A[0, j-1] ^ A[0, k]
# 3: X ^ Y = T => X ^ Y ^ Y = T ^ Y => X = T ^ Y

# So? 
# A[i,j) = A[j,k]
# A[0,i) ^ A[0,j) = A[0,j) ^ A[0,k]

# i < j <= k
# A[i,j-1] = A[j,k]
#   => A[0,i-1] ^ A[0, j-1] = A[0,j-1] ^ A[0,k] => A[0,i-1] = A[0,k]，此时 j 为 k - i 个. (i > 0)
# if i = 0? 
#   => A[-1,i-1]^A[-1,j-1] = A[-1,j-1]^A[-1,k]
#         A[-1,-1] =? so A[-1,-1]=0, A[-1,-1]^A[0,0] = A[0,0] = A[-1,0]
class Solution:
    def countTriplets(self, arr) -> int:
        res = 0
        cur = arr[0]
        pre = {0:[-1]}
        if cur in pre: pre[cur].append(0)
        else: pre[cur] = [0]

        for k in range(1, len(arr)):
            cur = cur ^ arr[k]
            if cur in pre:
                i_list = pre[cur]  # A[0,i-1] = A[0,k], i<k => i-1 < k-1
                for i_minus_1 in i_list:
                    if i_minus_1 < k - 1:
                        res += k - (i_minus_1+1)
                i_list.append(k)
            else:
                pre[cur] = [k]
        return res

print (Solution().countTriplets([2,3,1,6,7]))
print (Solution().countTriplets([2,3]))
print (Solution().countTriplets([1,3,5,7,9]))
print (Solution().countTriplets([7,11,12,9,5,2,7,17,22]))
print (Solution().countTriplets([1,1,1,1,1])) # wrong 6, exp 10
