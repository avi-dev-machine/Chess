# Chess Game vs Computer

A web-based chess game where you can play against the **Stockfish** chess engine.

## 🚀 Features
- **Play against Stockfish AI**: Challenge yourself with one of the strongest chess engines.
- **Interactive Chess Board**: Enjoy a visually appealing board with coordinates for easier navigation.
- **Move Validation**: Automatically validate moves to ensure the rules of chess are followed.
- **Move History Tracking**: Keep track of all the moves made during the game.
- **Algebraic Notation**: Enter moves in standard algebraic notation (e.g., `e2e4`, `Nf3`).
- **Reset Game**: Easily start a new game without reloading the page.

## 🛠️ Setup

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/chess-vs-computer.git
cd chess-vs-computer
2. Install Requirements
Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install flask python-chess
3. Download Stockfish
Download the Stockfish engine from Stockfish Chess Download.
Extract the Stockfish binary to the project folder.
4. Update Stockfish Path
In the app.py file, update the path to the Stockfish engine:

python
Copy code
stockfish_path = "path_to_stockfish_binary"
5. Run the Application
Start the Flask application:

bash
Copy code
python app.py
6. Open the Game
Once the server is running, open your browser and go to:

arduino
Copy code
http://localhost:5000
🎮 How to Play
Enter Moves: Type your moves in algebraic notation (e.g., e2e4, Nf3) into the input box.
Make Move: Click the "Make Move" button or press Enter after typing a move.
Computer Response: After you make a move, the computer will automatically respond with its best move.
Start a New Game: Click the "New Game" button to reset the game and start fresh.
🧑‍💻 Tech Stack
Python: The backend logic is powered by Python.
Flask: A lightweight web framework used to serve the game.
python-chess: A library to handle chess rules and game logic.
Stockfish: The AI engine to play against.
jQuery: For handling frontend interactions and AJAX requests.