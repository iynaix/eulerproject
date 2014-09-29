def euler67():
    with open("triangle67.txt") as fp:
        tri = [ln.strip() for ln in fp.read().splitlines()]
        tri = [[int(x) for x in ln.split()] for ln in tri]

    #iterate lines from the back of the triangle, reducing the triangle
    #by calculating a row of maximal sums
    new_row = tri[-1][:]
    for line in reversed(tri[:-1]):
        tmp = []
        for idx, num in enumerate(line):
            left = new_row[idx]
            right = new_row[idx + 1]
            tmp.append(num + max(left, right))
        new_row = tmp[:]
    return new_row.pop()
