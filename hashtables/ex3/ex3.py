def intersection(arrays):
    cache = {}
    for i in range(len(arrays)):
        for x in arrays[i]:
            if x not in cache:
                cache[x] = 1
            else:
                cache[x] +=1
    arr = []                
    for key, value in cache.items():
        if value >= len(arrays):
            arr.append(key)

    return arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
