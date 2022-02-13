
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter = 0
    for i in range(0, n):
        for j in range(0, n):
            if i>=j:
                continue
            print('ar{} + ar{} = {} + {} = {}'.format(i, j, ar[i], ar[j], ar[i]+ar[j]))
            if (ar[i]+ar[j]) % k == 0:
                counter+=1
    return counter
    
if __name__ == '__main__':
    result = divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
    print(result)