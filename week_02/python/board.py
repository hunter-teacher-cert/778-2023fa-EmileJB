class Board:
  error_char = '?' 

  def __init__(self,r,c,default_character=' '):
    if (r < 1):
      r = 1
    
    if (c < 0):
      c = 0
    
    self.rows = r
    self.columns = c
    self.board = [[default_character] * c for i in range(r)]
    self.default_char = default_character

  def getCell(self,r,c):
    if (r >= 0 and r < self.rows and c >= 0 and c < self.columns):
      return self.board[r][c]
    else:
      return self.error_char

  def setCell(self,r,c,new_char):
    if (r >= 0 and r < self.rows and c >= 0 and c < self.columns):     
      self.board[r][c] = new_char;

  def getRows(self):
    return self.rows

  def getColumns(self):
    return self.columns

  def clearBoard(self):
    for i in range(self.rows):
      for j in range(self.columns):
        self.board[i][j] = self.default_char

  def printBoard(self):
    for row in self.board:
      for cell in row:
        print(cell, end='')
      print()