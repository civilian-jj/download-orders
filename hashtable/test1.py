def fibo(n):
    if n <= 1:
        return 1
    
    
    l = [1,1]

    for i in range(2,n+1):
        l.append(l[i-2]+l[i-1])

    return l[n]

s = 'wxyzabyaadfaafafagadfaagagagaewg'
n = len(s)


l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ns = ''
for i in range(n):
    if i % 2 == 0:
        moves = -fibo(i)

    else:
        moves = fibo(i)
    ind = l.index(s[i])
    while ind >25 :
        ind -= 26
    while ind < -26 :
        ind += 26


    new_ind = ind + moves
    while new_ind >25 :
        new_ind -= 26
    while new_ind < -26:
        new_ind += 26
    print(new_ind)
    news = l[new_ind]
    ns += news


print(ns)

print(fibo(200))


def maxlevels(nums):

    
    # [1 2 3 5 6 1]
    n = len(nums)
    maxl = 0
    maxlength = max(nums)
    mm = min(nums) + max(nums)
    max_num = nums.count(maxlength)
    dic1 = {i:0 for i in range(1,maxlength)}
    dic2 = {i:0 for i in range(1,mm+1)}
    for i in nums:
        dic2[i] += 1
        if i != maxlength:
            dic1[i] += 1
    flag = 0
    for i in dic2:
        if dic1[i] != dic1[mm-i]:
            flag = False
    for i in dic1:
        if dic1[i] != dic1[maxlength-i]:
            flag = False
    else:
        max_l = (n - max_num)//2 + max_num
    

t = input().split()

t = [int(x) for x in t]

print(maxlevels(t))


