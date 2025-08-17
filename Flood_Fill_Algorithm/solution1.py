def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != oldColor:
            return
        image[r][c] = newColor
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image
