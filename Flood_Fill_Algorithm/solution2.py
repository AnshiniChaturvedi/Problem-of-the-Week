from collections import deque

def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image

    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if image[r][c] == oldColor:
            image[r][c] = newColor
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    q.append((nr, nc))
    return image
