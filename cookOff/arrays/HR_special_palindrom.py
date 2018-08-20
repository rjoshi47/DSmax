'''
https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
Special Palindrom: eith all chars in substring are same or only middle one is different like aabaa, nnMnn
We build frequency list and check if middle element frequescy is one.
like for: aabaaann
list be like (a,2)(b,1)(a,3)(n,2)
so for i = 1 i.e. (b,1)
we check if i-1 and i+1 have same characters and frequency of i is 1
'''
def substrCount(n, s):
    pal = []
    count = 0
    cur = None

    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                pal.append((cur, count))
            cur = s[i]
            count = 1
    pal.append((cur, count))

    ans = 0
        
    for i in pal:
        ans += (i[1] * (i[1] + 1)) // 2
    #print(ans)

    for i in range(1, len(pal) - 1):
        if pal[i - 1][0] == pal[i + 1][0] and pal[i][1] == 1:
            ans += min(pal[i - 1][1], pal[i + 1][1])
    #print(ans)
    return ans

n = int(input())
s = input()
print(substrCount(n, s))
