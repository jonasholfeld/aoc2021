import json
import pprint
with open('input.json') as jsonFile:
    entries = json.load(jsonFile)['entries']
    jsonFile.close()

# Part I
# counteasy = 0
# for entry in entries:
#     output = entry.split(" | ")[1]
#     parts = output.split()
#     for part in parts:
#         if len(part) in [2, 4, 3, 7]:
#             counteasy += 1
#print(counteasy)

# Part II
from solve_code import solveCode, split, decode
values = []
for line in entries:
    signalPattern = line.split(" | ")[0]
    mapping = solveCode(signalPattern)
    input = line.split(" | ")[1].split()
    intstring = ""
    for i in input:
        intstring += str(decode(i, mapping))
    values.append(int(intstring))

print(sum(values))