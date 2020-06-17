'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # initialize first window
    window = nums[:k]
    # get first max value
    current_max = max(window)
    # store first max value
    maxes = [current_max]

    # iterate over the rest of the values
    for i, x in enumerate(nums[k:]):
        # add newest value to window
        window.append(x)
        # remove oldest value from window, and, 
        # if it equals the current max,
        # then recalculate the current max
        if window.pop(0) == current_max:
            current_max = max(window)
        # oldest value wasn't max, check if newest value is max
        elif x > current_max:
            current_max = x
        # store maximum for this window
        maxes.append(current_max)

    return maxes


    # maxes = [0] * (len(nums) - k + 1)
    # for i in range(len(maxes)):
    #     maxes[i] = max(nums[i:i+k])

    # return maxes

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
