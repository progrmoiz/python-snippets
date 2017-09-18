def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute(rest):
                yield seq[i:i+1] + x

def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute(rest):
                res.append(seq[i:i+1] + x)
    return resn

for i in permute('maths'):
    print(i)
