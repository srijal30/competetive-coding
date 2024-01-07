patterns = open(0).read().split("\n\n")
ans1 = 0
for p in patterns:
    rows = p.splitlines()
    cols = ["".join([r[x] for r in rows]) for x in range(len(rows[0]))]
    v = h = 0
    ver = []
    hor = []
    for i in range(1, len(rows[0])):
        valid = []
        for r, row in enumerate(rows):
            l = min(i, len(rows[0])-i)
            if row[:i][::-1][:l] == row[i:][:l]:
                valid.append(r)
        ver.append(valid)
    for i in range(1, len(cols[0])):
        valid = []
        for c, col in enumerate(cols):
            l = min(i, len(cols[0])-i)
            if col[:i][::-1][:l] == col[i:][:l]:
                valid.append(c)
        hor.append(valid)
    smudge_v = [i for i, x in enumerate(ver) if len(x)==len(rows)-1]
    smudge_h = [i for i, x in enumerate(hor) if len(x)==len(rows[0])-1]
    if smudge_v:
        ans1 += smudge_v[0]+1
    else:
        ans1 += 100*(smudge_h[0]+1)

print(ans1)

