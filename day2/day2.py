import json
with open('input_day2.json') as file:
    commands = json.load(file)['commands']

submarine = {
    'horizontal': 0,
    'depth': 0,
    'aim': 0
}

def up(amount):
    submarine['aim'] -= amount

def down(amount):
    submarine['aim'] += amount

def forward(amount):
    submarine['horizontal'] += amount
    submarine['depth'] += submarine['aim'] * amount

for command in commands:
    if command.startswith('forward'):
        forward(int(command.split()[-1]))
    if command.startswith('down'):
        down(int(command.split()[-1]))
    if command.startswith('up'):
        up(int(command.split()[-1]))

print(submarine['horizontal'] * submarine['depth'])