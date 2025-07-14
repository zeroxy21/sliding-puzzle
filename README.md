# Sliding Puzzle Solver (3x3 & 4x4)

This project is a demonstration of algorithmic methods for solving the **sliding puzzle** (also known as the *15-puzzle* or *jeu du taquin* in French), implemented in Python. It features two distinct approaches for solving 3x3 and 4x4 puzzles, with functions for evaluating, transforming, and scoring puzzle configurations.

## 🧠 Project Purpose

This is not a graphical game, but an **algorithmic exploration** of how to evaluate and solve sliding puzzles using Python logic and scoring functions. It can serve as a base for academic work, AI heuristics, or puzzle analysis.

---

## 📂 Project Structure

- `bab taille 3.py`:  
  A resolution method for 3x3 puzzles using scoring heuristics.

- `methode generale de resolution 4x4.py`:  
  A generalized method tailored to solving 4x4 puzzles.

- `Copie de Copie de Le Jeu du Taquin.pdf`:  
  (Optional) A French-language document explaining the concepts and methods.

- `.gitignore`, `.gitattributes`:  
  Standard Git configuration files.

---

## 🧩 Features

- Convert puzzle grids between 2D (list of lists) and 1D (flat list) formats.
- Score puzzle states based on similarity to the target configuration.
- Modular functions for reuse in custom solving strategies.

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### How to Run

```bash
python "bab taille 3.py"
python "methode generale de resolution 4x4.py"

These scripts execute algorithmic logic and print intermediate results (they do not offer a UI or interactive game loop).

test = [[1, 2, 3],
        [6, 5, 4],
        [9, 7, 8]]

score = score_tab(test, solution)

test = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 15, 14, 16]]

score = score_tab_1(test, solution)




