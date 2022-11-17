#!/usr/bin/env python3
import sys

spaces = []
for i in range(0, 14):
    spaces.append(1)
spaces.append(0)

links = []
for i in range(0, 15):
    links.append({})


def linkRight(a, b):
    global links
    links[a]['right'] = b
    links[b]['left'] = a


def linkUpRight(a, b):
    global links
    links[a]['upright'] = b
    links[b]['downleft'] = a


def linkDownRight(a, b):
    global links
    links[a]['downright'] = b
    links[b]['upleft'] = a


for i in range(0, 4):
    linkRight(i, i+1)
    linkUpRight(i, i + 5)

for i in range(5, 8):
    linkRight(i, i + 1)
    linkDownRight(i, i - 4)
    linkUpRight(i, i + 4)

for i in range(8, 9):
    linkDownRight(i, i - 4)

for i in range(9, 11):
    linkRight(i, i + 1)
    linkDownRight(i, i - 3)
    linkUpRight(i, i + 3)

for i in range(11, 12):
    linkDownRight(i, i - 3)

for i in range(12, 13):
    linkRight(i, i + 1)
    linkDownRight(i, i - 2)
    linkUpRight(i, i + 2)

for i in range(13, 14):
    linkDownRight(i, i - 2)

for i in range(14, 15):
    linkDownRight(i, i - 1)

print(links)


def findSolutionsRecursively(spaces, moves):
    global links
    foundSomething = False
    for i in range(0, 15):
        if tryAllJumps(spaces, i, moves):
            foundSomething = True
    if not foundSomething:
        if sum(spaces) == 1:
            print("FOUND A SOLUTION BOIIII")
            print(moves)
            sys.exit(0)


def tryAllJumps(spaces, index, moves):
    foundSomething = False
    for direction in ['right', 'left', 'upright', 'upleft', 'downright', 'downleft']:
        if tryJump(spaces, index, direction, moves):
            foundSomething = True
    return foundSomething


def tryJump(spaces, index, direction, moves):
    newspaces = []
    for i in range(0, 15):
        newspaces.append(spaces[i])
    spaces = newspaces
    newmoves = []
    for i in range(0, len(moves)):
        newmoves.append(moves[i])
    moves = newmoves
    if not spaces[index]:
        return False
    if direction not in links[index]:
        return False
    if not spaces[links[index][direction]]:
        return False
    if direction not in links[links[index][direction]]:
        return False
    if spaces[links[links[index][direction]][direction]]:
        return False
    spaces[index] = 0
    spaces[links[index][direction]] = 0
    spaces[links[links[index][direction]][direction]] = 1
    moves.append("jump from peg " + str(index) + " in direction " + direction)
    findSolutionsRecursively(spaces, moves)
    return True


findSolutionsRecursively(spaces, [])
