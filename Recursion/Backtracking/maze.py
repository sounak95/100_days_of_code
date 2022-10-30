


def path(p, r, c):
    if r==1 and c==1:
        print(p)
        return

    if r>1:
        path(p+'D', r-1, c)

    if c>1:
        path(p+'R', r, c-1)

def pathRet(p, r, c):
    if r==1 and c==1:
        l1=[]
        l1.append(p)
        return l1

    l1=[]
    if r>1:
        l1.extend(pathRet(p+'D', r-1, c))

    if c>1:
        l1.extend(pathRet(p+'R', r, c-1))

    return l1

def pathCount(p, r, c):
    if r==1 and c==1:
        return 1

    count=0
    if r>1:
        count+=pathCount(p+'D', r-1, c)

    if c>1:
        count+=pathCount(p+'R', r, c-1)

    return count

def pathRetDiagonal(p, r, c):
    if r==1 and c==1:
        l1=[]
        l1.append(p)
        return l1

    l1=[]
    if r>1 and c>1:
        l1.extend(pathRetDiagonal(p+'D', r-1, c-1))
    if r>1:
        l1.extend(pathRetDiagonal(p+'V', r-1, c))

    if c>1:
        l1.extend(pathRetDiagonal(p+'H', r, c-1))

    return l1

def pathRestrictions(p, maze , r, c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return

    if not maze[r][c]:
        return

    if r<len(maze)-1:
        pathRestrictions(p+'D', maze, r+1, c)

    if c< len(maze[0])-1:
        pathRestrictions(p+'R', maze, r, c+1)


if __name__ == "__main__":
    path("", 3, 3)
    print(pathRet("", 3, 3))
    print(pathCount("", 3, 3))
    print(pathRetDiagonal("", 3, 3))
    board =[
        [True, True, True],
        [True, False, True],
        [True, True, True]
    ]
    pathRestrictions("", board, 0, 0)