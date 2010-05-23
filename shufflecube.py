#!/usr/bin/env python

"""
Cube Shuffle

Generate random Rubik's Cube moves useful for honestly shuffling the cube.

Stephen Mann
April 2010
"""

import random

sides = ["L", "R", "U", "D", "F", "B"]
directions = ["", "'", "2"]

def move(blackListedSide=""):
  """Return a single random move."""
  validSides = [side for side in sides if side not in blackListedSide]
  return random.choice(validSides) + random.choice(directions)

def moves(count):
  """Return a list of count random moves."""
  lastMove = ""
  movesList = []
  for i in range(count):
    lastMove = move(lastMove)
    movesList.append(lastMove)
  return movesList

def prettyMoves(count):
  """Return a pretty list of count random moves."""
  return " ".join([m for m in moves(25)])

if __name__ == "__main__":
  print prettyMoves(25)
