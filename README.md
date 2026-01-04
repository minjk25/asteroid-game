# Asteroid Game

This is my first game ever created using **Pygame**.

The purpose of this repository is to learn **Python** in general and get hands-on experience with:
- Game loops
- Event handling
- Basic object-oriented programming
- Collision detection

## Gameplay
A simple Asteroids-style game where the player controls a ship and avoids or shoots asteroids.

## Requirements
- Python 3.13
- [uv](https://docs.astral.sh/uv/) installed
- Operating system: Linux or macOS (Windows not officially supported)

## How to run
```bash
# 1. Clone
git clone https://github.com/minjk25/asteroid-game.git
cd asteroid-game

# 2. Install dependencies (including pygame)
uv sync

# 3. Run the game
uv run main.py


## Controls

- `A` – Rotate ship left
- `D` – Rotate ship right
- `W` – Thrust (move forward)
- `S` – Reverse thrust (move backward)
- `Space` – Shoot
- `Ctrl + C` (in the terminal) – Quit the game