# https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/

cardPoints = [1,79,80,1,1,1,200,1]
k = 3

res = cur = sum(cardPoints[:k])
for i in range(1,k+1):
    cur = cur - cardPoints[k - i] + cardPoints[-i]
    if cur > res:
        res = cur

print (res)
