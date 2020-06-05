def has_negatives(a):
    # cache = {}
    # arr = []
    # for num in a:
    #      arr.append(abs(num))
    # print(arr)
    # for num in arr:
    #     if num not in cache:
    #         cache[num] = 1
    #     else:
    #         cache[num] += 1 
    # finalArr = []

    # for key, value in cache.items():
    #     if value >=2:
    #         finalArr.append(key)
    # return finalArr

    cache = {}
    sol = []
    for val in a:
        if val * -1 not in cache:
            cache[val] = val
        else:
            sol.append(abs(val))
    
    return sol




if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
