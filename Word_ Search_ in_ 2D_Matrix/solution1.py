def word_search(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check rows
    for row in matrix:
        if word in ''.join(row):
            return True

    # Check columns
    for col in range(cols):
        col_str = ''.join(matrix[r][col] for r in range(rows))
        if word in col_str:
            return True
    return False

# Example
matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]
print(word_search(matrix, "FOAM"))  # True
print(word_search(matrix, "MASS"))  # True
