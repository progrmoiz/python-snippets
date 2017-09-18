L, S = [1, 2, 3], 'spam'
# for i in range(len(S)):
    # S = S[1:] + S[:1]
    # print(S, end=' ')

# simple function
def scramble(seq):
    res = []
    for i in range(len(seq)):
        X = seq[1:] + seq[:1]
        res.append(X)
    return res


def scramble1(seq):
    return [seq[1:] + seq[:1] for i in range(len(seq))]

# above wait caller to wait until all list is done

# generator function
def scramble2(seq):
    for i in range(len(seq)):
        yield seq[1:] + seq[:1]

def scramble3(seq):
    return (seq[1:] + seq[:1] for i in range(len(seq)))

