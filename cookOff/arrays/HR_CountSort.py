'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
Fraudulent Activity Notifications
We calculate the median for window from (s-(s+d)) entries and send a notification if (s+d+1) element > 2*median.
Problem:
For input:
9 5
2 3 4 2 3 6 8 4 5
Maintain a window of 5
1. 2 3 4 2 3 -> sorted -> 2 2 3 3 4 median:3, next element is 6>=2*3 so +1 notification
2. 3 4 2 3 6 -> sorted -> 2 3 3 4 6 median:3, next element is 8>=2*3 so +1 notification.

To get median of fixed sized windows we use sub-routine of count-sort where we maintain 
the frequency array for elements in given window.
Based on window position we increment and decrement the element count in frequency array.

Then we create a prefix sum array preCount which will store the position of the element with index value.
preCount[4] = 2 indicates that value of 4 will be at index 2 in sortedarray.

'''
def getMedian(fcount, d):
    preCount = [0]*201 # max value of an element in array <= 200 
    preCount[0] = fcount[0]
    for k in range(1, 201):
        preCount[k] += preCount[k-1] + fcount[k]
    
    m = int(d/2)    
    a = m
    b = m + 1 # if d (window size is odd return this element only)
    
    aset = False
    bset = False
    
    for k in range(0, 201):
        if not aset and a <= preCount[k]:
            a = k
            aset = True
        if not bset and b <= preCount[k]:
            b = k
            bset = True
        if d % 2 == 0:
            if aset and bset:
                break
        elif bset:
            break
    print((a,b))
    if d % 2 == 0:
        return (a+b)/2
    else:
        return b    
    
(n, d) = input().split(" ")
n = int(n)
d = int(d)
nums = list(map(int, input().split(" ")))

fcount = [0]*201
for k in range(d):
    fcount[nums[k]] += 1
    
count = 0
for k in range(d, n):
    m = getMedian(fcount, d);
    if nums[k] >= 2*m:
        count += 1
    fcount[nums[k-d]] -= 1
    fcount[nums[k]] += 1
    
    
print(count)    
