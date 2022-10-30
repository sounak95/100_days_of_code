





def allPath(p, maze , r, c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return

    if not maze[r][c]:
        return

    maze[r][c] = False

    if r>0:
        allPath(p+'U', maze , r-1, c)

    if c>0:
        allPath(p+'L', maze , r, c-1)

    if r<len(maze)-1:
        allPath(p+'D', maze, r+1, c)

    if c< len(maze[0])-1:
        allPath(p+'R', maze, r, c+1)

    maze[r][c] = True


def allPathPrint(p, maze , r, c, path, step):
    if r==len(maze)-1 and c==len(maze[0])-1:
        path[r][c] = step
        for row in path:
            print(row)
        print(p)
        print()
        # path[r][c] = 0
        return

    if not maze[r][c]:
        return

    maze[r][c] = False
    path[r][c] = step

    if r>0:
        allPathPrint(p+'U', maze , r-1, c, path, step+1)

    if c>0:
        allPathPrint(p+'L', maze , r, c-1, path, step+1)

    if r<len(maze)-1:
        allPathPrint(p+'D', maze, r+1, c, path, step+1)

    if c< len(maze[0])-1:
        allPathPrint(p+'R', maze, r, c+1, path, step+1)

    maze[r][c] = True
    path[r][c] = 0


if __name__ == "__main__":
    board = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]
    # allPath("", board, 0, 0)
    path =[
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    allPathPrint("", board, 0, 0, path, 1)