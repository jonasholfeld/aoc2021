import json

with open('day1_input.json') as jsonFile:
    input = json.load(jsonFile)['input']
    jsonFile.close()

increased = 0
increased_windows = 0
windows = []

for i in range(len(input)):
    if(i>0):
        if(input[i] > input[i-1]):
            increased += 1
    if(i<len(input)-2):
        windows.append(input[i] + input[i+1] + input[i+2])


for i in range(len(windows)):
    if(i>0):
        if(windows[i] > windows[i-1]):
            increased_windows += 1

print(increased)
print(increased_windows)