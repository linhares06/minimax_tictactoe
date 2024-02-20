from pydantic import BaseModel


class Game(BaseModel):
    board: list
    turn: int