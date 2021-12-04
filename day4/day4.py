from board import Board
import json

def initialize():
    with open('input_day4.json') as jsonFile:
        draws = json.load(jsonFile)['draws']
        jsonFile.close()

    with open('input_day4_boards.txt') as f:
        lines = f.readlines()

    numberString = ''
    boards = []
    for line in lines:
        if (line == '\n'):
            boards.append(Board(list(map(lambda x: int(x), numberString.split()))))
            numberString = ''
        else:
            numberString += (line + ' ')

    return draws, boards

#Part 1
draws, boards = initialize()
breakloop = False
for draw in draws:
    if(breakloop): break
    for board in boards:
        board.markNumber(draw)
        if(board.checkCompleteness()):
            print(sum(board.getUnmarkedNumbers())*draw)
            breakloop = True
            break

#Part2
draws, boards = initialize()
final = 0
for draw in draws:
    for board in boards:
        if (not board.won):
            board.markNumber(draw)
            board.checkCompleteness()
            if(board.won):
                final = (sum(board.getUnmarkedNumbers())*draw)

print(final)