'''
Created on 28-May-2017

@author: rjoshi
'''
# public static double closestToT(double[] x, double t){
#   double prefix = 0;
#   TreeSet<Double> set = new TreeSet<Double>();
#   set.add(prefix);
#   double leastDiff = Double.MAX_VALUE;
#   
#   for(double i : x){
#     prefix += i; // the cumulative sum up to i
#     double rest = prefix - t; // how far away we are from t
#     if(set.first() <= rest){
#       double theSum = prefix - set.floor(rest);
#       leastDiff = Math.min(leastDiff, Math.abs(theSum - t));
#     }
#     if(set.last() >= rest){
#       double theSum = prefix - set.ceiling(rest);
#       leastDiff = Math.min(leastDiff, Math.abs(theSum - t));
#     }
#     set.add(prefix);
#   }
#   return leastDiff;
# }
import math
def test(nums, val):
    prefix = 0
    set1 = []
    set1.append(prefix)
    leastDiff = 1000000
    
    for i in range(0, len(nums)):
        prefix = prefix + i
        rest = prefix - val
        if set1[0] <= rest:
            tsum = prefix - math.floor(rest)
            leastDiff = min(leastDiff, abs(tsum-val))
        
        if set1[len(set1)-1] >= rest:
            tsum = prefix - math.ceil(rest)
            leastDiff = min(leastDiff, abs(tsum-val))

        set1.append(prefix)
        set1.sort()
    return leastDiff

l = [3,1,2,10,5,6]
l.sort()
print(test([1,2,4,3,6,5], 21))