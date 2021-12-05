import json

from numpy.lib.twodim_base import diag
from diagram import Diagram
import numpy as np

with open('input.json') as jsonFile:
    lines = json.load(jsonFile)['lines']
    jsonFile.close()

diagram = Diagram(1000, 1000)

for line in lines:
    xstart = int(line.split(' -> ')[0].split(',')[0])
    ystart = int(line.split(' -> ')[0].split(',')[1])
    xend = int(line.split(' -> ')[1].split(',')[0])
    yend = int(line.split(' -> ')[1].split(',')[1])
    diagram.drawLine(xstart, ystart, xend, yend)

print((diagram.diagram > 1).sum())