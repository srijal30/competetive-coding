rows = [l for l in open(0).read().splitlines()]
cols = ["".join([row[x] for row in rows]) for x in range(len(rows[0]))]

ex_rows = [x for x, row in enumerate(rows) if not "#" in row]
ex_cols = [y for y, col in enumerate(cols) if not "#" in col]
print(ex_rows, ex_cols, end="\n\n")

galaxies = []
for i, row in enumerate(rows):
    for j, ch in enumerate(row):
        if ch == "#":
            galaxies.append((i,j))

ans1 = 0
for gal1 in galaxies:
    x1, y1 = gal1
    for gal2 in galaxies:
        x2, y2 = gal2
        ans1 += abs(x1-x2) + abs(y1-y2)
        ans1 += (sum([x in range(min(x1, x2), max(x1, x2)) for x in ex_rows])*999999)
        ans1 += (sum([y in range(min(y1, y2), max(y1, y2)) for y in ex_cols])*999999)


print(ans1//2)



