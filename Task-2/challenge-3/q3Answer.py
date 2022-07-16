Resault = ""


def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2 * dy - dx
    y = 0
    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if D >= 0:
            y += 1
            D -= 2 * dx
        D += 2 * dy


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, head: Point, tail: Point):
        self.head = head
        self.tail = tail


def drawline(size: tuple, lines: list, chrs=('.', '*', ' ')) -> Resault:
    global Resault
    co = []
    for line in lines:
        co.extend(list(bresenham(
            line.head.x, line.head.y, line.tail.x, line.tail.y)))
    for column in range(size[1]):
        for row in range(size[0]):
            if (row, column) in co:
                Resault += chrs[1]
            else:
                Resault += chrs[0]
            if row != size[0]-1:
                Resault += chrs[2]*size[2]
        if column != size[1]-1:
            Resault += "\n"
    return Resault


if __name__ == "__main__":
    print('Input the numbers of row, column and number of separators between each point, separated by space')
    size = tuple(map(int, input().split()))
    print('Input the two points to draw line with, in the format of (x1,y1)-(x2,y2)')
    coordinates = [i[::-1] for i in [list(map(int, j.split(','))) for i in [
        i.split('-') for i in input().replace(')', '').replace(
            '(', '').split(' ')] for j in i]]
    coordinates = [coordinates[i-4:i] for i in range(4, len(coordinates)+4, 4)]
    
    lines = []
    for c in coordinates:
        lines.append(Line(Point(c[0][0], c[0][1]), Point(c[1][0], c[1][1])))
    print(drawline(size, lines))