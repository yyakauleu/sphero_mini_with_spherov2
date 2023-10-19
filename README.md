# Sphero Control Repository using spherov2

## Overview

This repository contains Python code to control a Sphero robot via keyboard inputs. It uses the `spherov2` package for Sphero interaction and the `keyboard` library for key detection. The program runs in a loop, listening for key presses to move the Sphero in different directions.

## Features

- **Real-time Control**: Control your Sphero robot in real-time using keyboard inputs.
- **Dynamic Loading**: Utilizes Python's `importlib` to dynamically reload control logic, making development easier.
- **Modular Design**: Control logic is separated into a `controls` module for easier management and updates.

## Dependencies

- Python 3.x
- `spherov2` package
- `keyboard` library

## How to Run

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `ex_control.py` to start the program.

## Keyboard Controls

- **W**: Move Forward
- **S**: Move Backward
- **A**: Move Left
- **D**: Move Right
- **Q**: Quit the program

