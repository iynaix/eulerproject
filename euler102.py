def euler102():
    def area_from_coords(xa, ya, xb, yb, xc, yc):
        #calculates the area of a triangle give the coords
        return abs((xa - xc) * (yb - ya) - (xa - xb) * (yc - ya)) / 2

    ret = 0
    with open("triangles102.txt", "rU") as fp:
        for line in fp.read().splitlines():
            coords = [float(p) for p in line.split(",")]
            total_area = area_from_coords(*coords)

            #compose 3 smaller triangles using the origin
            tri1 = area_from_coords(0, 0, *coords[:4])
            tri2 = area_from_coords(0, 0, *coords[-4:])
            tri3 = area_from_coords(0, 0, coords[0], coords[1], coords[4],
                                    coords[5])
            #the origin is within the triangle if the areas match up
            ret += total_area == tri1 + tri2 + tri3
    return ret
