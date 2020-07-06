'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], 0
        if arr[left] != 0:
            left = left + 1
        if arr[right] == 0:
            right = right - 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")