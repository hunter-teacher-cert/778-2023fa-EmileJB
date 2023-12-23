import sys
import time
from board import Board

class Cgol:
  def __init__(self, live_cell='X', dead_cell=' '):
    self.board = Board(25,25,dead_cell)
    self.live_cell = live_cell
    self.dead_cell = dead_cell

  def initializeBoard(self):
    self.board.clearBoard()

  def printBoard(self):
    return_string = ""
    rows = range(0,self.board.getRows())
    for row in rows:
      cols = range(0,self.board.getColumns())
      for col in cols:
        return_string += self.board.getCell(row,col) + " "
      return_string += "\n"
    print(return_string)

  def setCell(self,r,c,val):
    self.board.setCell(r,c,val)

  def getCellStatus(self,r,c):
    if (r >= self.board.getRows() or r < 0 or c < 0 or c >= self.board.getColumns()):
      return 0
    if (self.board.getCell(r,c) == self.live_cell):
      return 1
    else:
      return 0

  def countNeighbours(self,r, c):
    neighbor_count = self.getCellStatus(r-1,c-1) + self.getCellStatus(r,c-1) + self.getCellStatus(r+1,c-1) + self.getCellStatus(r-1,c) + self.getCellStatus(r+1,c) + self.getCellStatus(r-1,c+1) + self.getCellStatus(r,c+1) + self.getCellStatus(r+1,c+1);
    return neighbor_count

  def getNextGenCell(self,r, c):
    neighbor_count = self.countNeighbours(r, c)
    if (neighbor_count < 2 or neighbor_count > 3):
      return self.dead_cell
    elif (neighbor_count == 2):
      return self.board.getCell(r,c)
    else:
      return self.live_cell

  def generateNextBoard(self):
    rows = self.board.getRows()
    cols = self.board.getColumns()
    new_board = Board(rows,cols,self.dead_cell)

    for row in range(0,rows):
      for col in range(0,cols):
        new_cell = self.getNextGenCell(row,col)
        new_board.setCell(row,col,new_cell)

    
    self.board = new_board


  def animate(self, n):
    print("\033[2J",end="")
    sys.stdout.flush()
    print("\033[H",end="")
    sys.stdout.flush()
    print(f"Gen {n}:")
    self.printBoard()
  
    time.sleep(1)

  def play(self, max_generations):
    generation_count = 1
    while (generation_count <= max_generations):
      self.animate(generation_count)
      self.generateNextBoard()
      generation_count+=1

  def setSquareConfiguration(self):
    self.setCell(12, 12, self.live_cell)
    self.setCell(11, 12, self.live_cell)
    self.setCell(13, 12, self.live_cell)
    self.setCell(11, 11, self.live_cell)
    self.setCell(12, 11, self.live_cell)
    self.setCell(13, 11, self.live_cell)
    self.setCell(11, 13, self.live_cell)
    self.setCell(12, 13, self.live_cell)
    self.setCell(13, 13, self.live_cell)

  def setOtherConfiguration(self):
    self.setCell(12, 12, self.live_cell)
    self.setCell(13, 12, self.live_cell)
    self.setCell(11, 11, self.live_cell)
    self.setCell(13, 11, self.live_cell)
    self.setCell(11, 13, self.live_cell)
    self.setCell(13, 13, self.live_cell)

  def setMovingConfiguration(self):
    self.setCell(13, 12, self.live_cell)
    self.setCell(12, 11, self.live_cell)
    self.setCell(11, 13, self.live_cell)
    self.setCell(12, 13, self.live_cell)
    self.setCell(13, 13, self.live_cell)
  

demo = Cgol()
demo.initializeBoard()
demo.setOtherConfiguration()
demo.play(20)
  

    