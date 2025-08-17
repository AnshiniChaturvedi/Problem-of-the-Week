def word_search_transpose(matrix, word):
    rows = [''.join(r) for r in matrix]
    cols = [''.join(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
    return any(word in line for line in rows + cols)
