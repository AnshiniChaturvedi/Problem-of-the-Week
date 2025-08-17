def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_list(nums):
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(gcd_of_list(arr))
