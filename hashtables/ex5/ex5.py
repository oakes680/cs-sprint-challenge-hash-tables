# Your code here



def finder(files, queries):
    cache = {}
    for x in files:
        spl = x.split('/')
        if spl[len(spl) - 1] not in cache:
            cache[spl[len(spl) - 1]] = [x]
        else:
            cache[spl[len(spl) - 1]].append(x)
    finArr = []

    for q in queries:
        if cache.get(q) is not None:
            finArr.append(cache.get(q))

    return [item for sublist in finArr for item in sublist]




if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
