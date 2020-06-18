'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # validate input
    if n < 0:
        raise(ValueError('n cannot be less than zero'))

    # force use of cache
    if cache is None:
        return eating_cookies(n, [0 for _ in range(n+1)])

    # base cases
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif n == 3:
        cache[n] = 4

    # recursive cases
    # if not cached -> calculate and cache    
    if cache[n] == 0:
        cache[n] = (
            eating_cookies(n-1, cache) +
            eating_cookies(n-2, cache) +
            eating_cookies(n-3, cache)
        )

    # return cached result
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
