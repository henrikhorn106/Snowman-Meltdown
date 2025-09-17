# ❄️ Snowman-Meltdown

A fun little word-guessing game where you’re racing against the cold!  
Your mission: guess the hidden word before the snowman melts away. Each wrong guess brings him closer to disappearing forever. Can you save him in time?  

---

## 🎮 Gameplay  
- A random word is selected at the start.  
- You have a **limited number of attempts** (e.g., 8).  
- Each incorrect guess makes the snowman melt piece by piece (head, body, arms…).  
- If you guess the full word before he’s gone, you win.  
- If he melts completely, the game is over.  

---

## 🛠️ Installation & Start  
1. Clone the repository:  
   ```bash
   git clone https://github.com/henrikhorn106/snowman-saver.git
   cd snowman-saver

2. Run the game:
   ```bash
   python game_logic.py

---

## Requirements
Python 3.8+

📂 Project Structure
```bash
   snowman-meltdown/
   ├── game_logic.py     # Main game file (entry point)
   ├── words.py          # Word list / word generator
   ├── ascii_art.py      # Snowman ASCII drawings
   ├── README.md         # Project documentation
