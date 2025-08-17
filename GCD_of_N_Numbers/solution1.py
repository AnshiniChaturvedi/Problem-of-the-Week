import math
from functools import reduce

def gcd_of_list(nums):
    return reduce(math.gcd, nums)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(gcd_of_list(arr))