from game import make_move, find_best_move, CPU


class Play:
    MINIMAX_DEPTH = 9

    def __init__(self, board, turn):
        """
        Initializes a new instance of the Play class.

        Args:
            board (list): A list representing the game board.
            turn (int): An integer representing the current turn.
        """
        self.board = board
        self.turn = turn

    def get_cpu_best_move(self):
        """
        Gets the best move for the CPU player using the minimax algorithm and update the board.

        Returns:
            None.
        """
        position = find_best_move(self.board, self.MINIMAX_DEPTH - self.turn)
        self.board = make_move(position, self.board, CPU)
        self.turn += 1

    def remove_null_from_board(self):
        """
        Removes null values from the game board.

        Null values are replaced with their corresponding index positions.

        Returns:
            list: The modified game board.
        """
        self.board = [x if x is not None else y for x, y in zip(self.board, [1, 2, 3, 4, 5, 6, 7, 8, 9])]

    def set_null_on_board(self):
        """
        Sets null values on the game board.

        Values that are not 'X' or 'O' are replaced with null values.

        Returns:
            list: The modified game board.
        """
        self.board = [None if cell not in ['X', 'O'] else cell for cell in self.board]