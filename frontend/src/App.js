import { useState } from 'react';

const GAME_URL = 'http://localhost:8000/';
const HEADER = {'Content-Type': 'application/json'}

function Square({ value, onSquareClick, loading }) {
  return (
    <button className="square" onClick={onSquareClick} disabled={loading}>
      {value}
    </button>
  );
}

export default function Board() {
  const [squares, setSquares] = useState(Array(9).fill(null));
  const [loading, setLoading] = useState(false)
  let [turn, setTurn] = useState(0);
  let gameStatus = '';
  
  async function handleClick(i) {
    if (squares[i] || calculateWinner(squares)) {
      return;
    }

    setLoading(true)
    
    const nextSquares = squares.slice();
    const updateTurn = turn + 1;
    nextSquares[i] = "X";
  
    setSquares(nextSquares);
    setTurn(updateTurn);

    if (updateTurn >= 9) {
      return;
    }

    const getCpuMove = async (board, turn) => {
      try {
        const response = await fetch(GAME_URL, {
          method: 'POST',
          headers: HEADER,
          body: JSON.stringify({ board, turn }),
        });
        const data = await response.json();
        setSquares(data.board);
        setTurn(data.turn);
      } catch (error) {
        gameStatus = 'Error connecting to server.'
        console.error('Error:', error);
      } finally {
        setLoading(false)
      }
    };

    getCpuMove(nextSquares, updateTurn);
  }
  
  const winner = calculateWinner(squares);
  const tie = calculateTie(squares);

  if (winner) {
    gameStatus = `Winner: ${winner}`;
  } else if (tie) {
    gameStatus = 'Tie!';
  }

  return (
    <>
      <h1>A Tic Tac Toe Game!</h1>
      <div className="board-row">
        <Square value={squares[0]} onSquareClick={() => handleClick(0)} loading={loading}/>
        <Square value={squares[1]} onSquareClick={() => handleClick(1)} loading={loading}/>
        <Square value={squares[2]} onSquareClick={() => handleClick(2)} loading={loading}/>
      </div>
      <div className="board-row">
        <Square value={squares[3]} onSquareClick={() => handleClick(3)} loading={loading}/>
        <Square value={squares[4]} onSquareClick={() => handleClick(4)} loading={loading}/>
        <Square value={squares[5]} onSquareClick={() => handleClick(5)} loading={loading}/>
      </div>
      <div className="board-row">
        <Square value={squares[6]} onSquareClick={() => handleClick(6)} loading={loading}/>
        <Square value={squares[7]} onSquareClick={() => handleClick(7)} loading={loading}/>
        <Square value={squares[8]} onSquareClick={() => handleClick(8)} loading={loading}/>
      </div>
      <div className="status">{gameStatus}</div>
    </>
  );
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (const line of lines) {
    const [a, b, c] = line;
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

function calculateTie(squares) {
  return squares.every(element => element !== null);
}