# CyberSoul
### What is the cost of progress?

---

This is a tech demo of a game inspired by games like Cyberpunk and Shadowrun.
At present, it is only showing that just about everything works. It is very rough and very unfair as of this build.

---

![Coming from all sides](/demo_screen.png)

---

## How to Install

Clone

```
git clone https://github.com/drachelehre/CyberSoul
cd CyberSoul
python3 -m venv .venv

pip install -r requirements.txt
#you only need to install once
```

```
#to play make sure you activate the virtual environment
source .venv/bin/activate
# if windows .venv\Scripts\activate.bat
python main.py
```

---

## How to play:

#### Gameplay

Begin by entering a name (for saving the game)

WASD to move and mouse to aim, shoot and slash

You start with 100 HP and 1000 Humanity, if either goes to 0, it's Game Over

You can gain parts by defeating enemies, or purchasing them with Credits.
Equipping them costs Humanity

#### Shops


Shops spawn in a corner every once in a while. Approach them to open shop menu.

Buying is showing first. If you want to sell to afford something else or make room, press "C"

Use arrow keys to navigate. Press "Enter" buy/sell.

#### Inventory

Enter by pressing "E."
To equip a new item, press "Enter"

#### Saving/Loading

To save your progress, press "ESC" to enter pause menu and press "S" to save.

To load, at main menu press "L" and input the name of desired save.

---

## Under the Hood

- Infinitely spawning enemies
- Randomized parts of various conditions
- Randomized shops
- Made with Python using Pycharm library