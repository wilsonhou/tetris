class Board:
  def __init__(self):
    self.score = 0 # Score is number of rows cleared
    # * Board is 10x20 but you can create 10x24 to allow for more space
    self.board = [
      [' ' for _ in range(10)] for _ in range(24)
    ]
  
  def is_over(self):
    '''Returns whether or not the game board is complete'''
    # TODO: Figure out the lose condition. How do we check if game is over?
    pass

  def is_full(self, row):
    '''Returns whether or not a row is full'''
    return all(item == '*' for item in row)

  def reset_row(self, row):
    '''Resets Row to Empty'''
    if not is_full(row):
      # Check row is complete first
      return

    # Get rid of full row
    self.board.pop(self.board.index(row))
    self.board.insert(0, [' ' for _ in range(10)])

  def inc_score(self, count=1):
    self.score += count