#!/user/bin/python3
def maxConsecutiveSum(arr, k):
    max_sum = sum(arr[:k])
    window_sum = max_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [9, 3, 4, 5, 6, 7,]
print(maxConsecutiveSum(arr, 3))
