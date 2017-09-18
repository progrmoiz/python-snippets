def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


# def mymap(func, *seqs):
    # return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2], [2, 3, 4]))


def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


def mymap(func, *seqs):
    return (func(args) for args in zip(*seqs))

print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(list(mymap(pow, [1, 2], [2, 3, 4])))
