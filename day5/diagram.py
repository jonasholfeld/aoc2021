import numpy as np

class Diagram:

    def __init__(self, xDim, yDim) -> None:
        self.diagram = np.zeros((xDim, yDim))

    def drawLine(self, xStart, yStart, xEnd, yEnd):
        #horizontal line
        if(yStart == yEnd):
            if(xEnd < xStart):
                end = xEnd
                xEnd = xStart
                xStart = end
            for i in range(xStart, xEnd+1):
                self.diagram[i, yStart] += 1

        #vertical line
        elif(xStart == xEnd):
            if(yEnd < yStart):
                end = yEnd
                yEnd = yStart
                yStart = end
            for i in range(yStart, yEnd+1):
                self.diagram[xStart, i] += 1

        #diagonal line
        else:
            if(xStart < xEnd and yStart < yEnd):
                while(xStart <= xEnd):
                    self.diagram[xStart, yStart] += 1
                    xStart += 1
                    yStart += 1
            elif(xStart > xEnd and yStart > yEnd):
                while(xStart >= xEnd):
                    self.diagram[xStart, yStart] += 1
                    xStart -= 1
                    yStart -= 1
            elif(xStart < xEnd and yStart > yEnd):
                while(xStart <= xEnd):
                    self.diagram[xStart, yStart] += 1
                    xStart += 1
                    yStart -= 1
            elif(xStart > xEnd and yStart < yEnd):
                while(xStart >= xEnd):
                    self.diagram[xStart, yStart] += 1
                    xStart -= 1
                    yStart += 1
