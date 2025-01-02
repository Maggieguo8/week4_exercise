import numpy as np  # noqaF401
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([[0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0]])

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """The Game class takes the argument 'size' to initialize."""

    def __init__(self, size):
        """Initialize the Game."""
        self.board = np.zeros((size, size))

    def play(self):
        """Start the game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Move to the next round based on current values."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbourcount = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (neighbourcount[i, j] == 3
                                         or (neighbourcount[i, j] == 2
                                             and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """Set the value of given position to life or death."""
        self.board[key] = value

    def show(self):
        """Display the current state."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, square):
        """
        Insert modifies the game board.

        As to insert the pattern provided at a location centred on the location
        given by the pair of integers.
        """
        if len(pattern.grid) % 2:
            step = len(pattern.grid) // 2
            key = (slice(square[0]-step, square[0]+step+1),
                   slice(square[1]-step, square[1]+step+1))
            self.__setitem__(key, pattern.grid)

        else:
            NotImplemented


class Pattern:
    """
    New Class Pattern.

    A pattern such as a glider maintains its behaviour,
    if translated, reflected or rotated.
    """

    def __init__(self, grid):
        """Grid is a numpy array of 1s and 0s."""
        self.grid = grid

    def flip_vertical(self):
        """
        Upside down reflection of Pattern.

        Returns a new Pattern whose rows are in reversed order,
        so that the pattern is upside down.
        """
        return Pattern(self.grid[::-1])

    def flip_horizontal(self):
        """
        Reflection of Pattern.

        Returns a new Pattern whose rows are in reversed order,
        so that the pattern is reversed left-right.
        """
        grid_new = np.array([rows[::-1] for rows in self.grid])
        return Pattern(grid_new)

    def flip_diag(self):
        """
        Flip around the diagonal.

        Returns a new pattern which is the transpose of the original.
        """
        return Pattern(np.transpose(self.grid))

    def rotate(self, n):
        """
        Rotation of Pattern.

        Return a new Pattern which is the original pattern rotated
        through n right angles anticlockwise.
        """
        if n == 0:
            return self
        elif n % 4 == 1:
            return self.flip_horizontal().flip_diag()
        else:
            return self.rotate(n-1).flip_horizontal().flip_diag()
