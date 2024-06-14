# Exercise: Boggle Game
def valid_word(word, dictionary):
    return word in dictionary

def search_word(board, row, col, word, visited, dictionary):
    if not (0 <= row < len(board) and 0 <= col < len(board[0])) or visited[row][col]:
        return
    word = word + board[row][col]
    if valid_word(word, dictionary):
        print(word)
    visited[row][col] = True
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            search_word(board, row + dr, col + dc, word, visited, dictionary)
    visited[row][col] = False

print("Enter the Boggle Board (separate rows by space):")
board = [input().split() for _ in range(3)]

print("Enter the List of Words (separate words by space):")
dictionary = set(input().split())

visited = [[False] * len(board[0]) for _ in range(len(board))]

for i in range(len(board)):
    for j in range(len(board[0])):
        search_word(board, i, j, "", visited, dictionary)
