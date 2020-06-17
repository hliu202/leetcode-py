def maxScoreSightseeingPair(self, A: List[int]) -> int:
    buff = A[0] # 初始buff
    ans = 0
    for j in range(1, len(A)):
        # 随着时间推移，buff的效力不断减少
        # 初始效力为某个A[i], i < j
        # 随时间减少的效力正好为 j - i
        # 因此当前buff的剩余效力恰为 A[i] + i - j
        buff -= 1
        # 根据当前buff默默算一下自己的战斗力（战5渣..)
        ans = max(ans, A[j] + buff)
        # 看看当前buff剩余效力有没有刷新buff好，没有则刷新buff
        buff = max(buff, A[j])
    return ans

# 作者：dan-huang-jiang-xing-ren
# 链接：https://leetcode-cn.com/problems/best-sightseeing-pair/solution/lai-lai-lai-gei-zi-ji-jia-ge-buff-by-dan-huang-jia/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。