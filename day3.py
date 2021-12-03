import json
import pprint

with open('input_day3.json') as file:
    powerconsumption = json.load(file)['powerconsumption']

bits = {}

for index in range(0, 12):
    bits[index] = {
        0: 0,
        1: 0
    }

for number in powerconsumption:
    for index in range(0, len(number)):
        bits[index][int(number[index])] +=1

gammarate = ''
epsilon = ''

for index in range(0, 12):
    gammarate += str(0 if bits[index][0] > bits[index][1] else 1)
    epsilon += str(0 if bits[index][0] < bits[index][1] else 1)

#print(int(gammarate, 2) * int(epsilon, 2))

oxygen = powerconsumption
co2 = powerconsumption

def bitcriteria_oxygen(number, index, bitdict):
    if(bitdict[index][0] == bitdict[index][1]):
        return int(number[index]) == 1
    else:
        return int(number[index]) == (0 if (bitdict[index][0] > bitdict[index][1]) else 1)

def bitcriteria_co2(number, index, bitdict):
    if(bitdict[index][0] == bitdict[index][1]):
        return int(number[index]) == 0
    else:
        return int(number[index]) == (0 if (bitdict[index][0] < bitdict[index][1]) else 1)

def countbits(array):
    bitdict = {}
    for index in range(0, 12):
        bitdict[index] = {
            0: 0,
            1: 0
        }
    for number in array:
        for index in range(0, len(number)):
            bitdict[index][int(number[index])] +=1
    return bitdict

for index in range(0, 12):
    bitdict = countbits(oxygen)
    if(len(oxygen) == 1):
        break
    oxygen = list(filter(lambda number: bitcriteria_oxygen(number, index, bitdict), oxygen))

for index in range(0, 12):
    bitdict = countbits(co2)
    if(len(co2) == 1):
        break
    co2 = list(filter(lambda number: bitcriteria_co2(number, index, bitdict), co2))


#print(co2)
print(int(oxygen[0], 2) * int(co2[0], 2))