from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import Game
from .play import Play


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/", response_model=Game)
async def get_cpu_move(data: Game):
    """
    Receives a Game object, processes it using the Play class, and returns the updated Game object.

    Args:
        data (Game): The Game object containing the current board state and turn.

    Returns:
        Game: The updated Game object after processing.
    """
    play: Play = Play(board=data.board, turn=data.turn)
    
    play.remove_null_from_board()
    play.get_cpu_best_move()
    play.set_null_on_board()

    data.board = play.board
    data.turn = play.turn

    return data
