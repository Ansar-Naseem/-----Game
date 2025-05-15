🐍 Snake-Water-Gun Game 🎮
A fun terminal-based Python game inspired by the classic Rock-Paper-Scissors, but with a twist: Snake, Water, and Gun.
You play against the computer, and the game continues until you lose. Try to score as high as you can! 🏆

🧩 Project Structure
bash
Copy
Edit
📁 Snake-Water-Gun-Game/
│
├── 🐍 snake,water,gun.py     # Version 1: Full condition-based logic
├── ⚡ snake,water,gun -concept.py     # Version 2: Optimized using math logic
└── 📄 README.md                 # You're here!

1️⃣ snake,water,gun.py – Full Logic Version

✅ Features:
Uses detailed if-else conditions
Maps numeric input to game choices (0 → Snake, 1 → Water, 2 → Gun)
Displays choices and outcome
Tracks score until the user loses

🖥️ Sample Output:
markdown
Copy
Edit
Enter snake(0),water(1) or gun(2): 2
--------------------------------------------------------------------------------------------
Computer choose : Water
User choose : Gun
--------------------------------------------------------------------------------------------
Congrats You Win!!

Enter snake(0),water(1) or gun(2): 0
--------------------------------------------------------------------------------------------
Computer choose : Gun
User choose : Snake
--------------------------------------------------------------------------------------------
Sorry You Loss!!
Your Final score is 1

2️⃣ snake,water,gun -concept.py – Optimized Logic Version

⚡ What's Different:
Same gameplay, but reduced conditions using math:
python
Copy
Edit
if (computer_move - user_input == 1) or (computer_move - user_input == -2):
    # User wins
Clean and elegant decision logic
Fewer lines, same fun 🎉

🔄 Game Logic:
You win if:
computer_move - user_input == 1 or -2
You lose otherwise (unless it's a draw)

📦 Requirements
Python 3.x

🙌 Contribution
Want to improve the game or add new features like multiplayer or GUI? Pull requests are welcome! 💡
