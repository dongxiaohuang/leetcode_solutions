class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        used = [[False]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j, used, 0):
                    return True
        return False

    def helper(self, board, word, i, j, used, idx):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board):
            return False
        if j < 0 or j >= len(board[0]):
            return False
        if word[idx] != board[i][j]:
            return False
        else:
            if used[i][j]:
                return False
            used[i][j] = True
            # move right
            if self.helper(board, word, i, j+1, used, idx+1):
                return True
            # move left
            if self.helper(board, word, i, j-1, used, idx+1):
                return True
            # move up
            if self.helper(board, word, i-1, j, used, idx+1):
                return True
            # move down
            if self.helper(board, word, i+1, j, used, idx+1):
                return True
            used[i][j] = False

        return False
