import json
from pprint import pprint
import sys, getopt
import os
import collections


'''
__author__ = "Peter Bangert"

__email__ = "petbangert@gmail.com"
__status__ = "Development"
'''


"""
	Session class handles all Session API applications
"""


class Scheduler:
    _grid, _vehicles, _rideamount,_bonus,_steps = 0,0,0,0,0
    _rides = []

    def __init__(self, filedata):  #
        x = first_line(filedata)

        self._grid = Grid(x[0],x[1])
        self._vehicles= x[2]
        self._rideamount = x[3]
        self._bonus = x[4]
        self._steps = x[5]
        self._rides = createRideObjs(filedata)



    def _getGrid(self, session=None):
        return self._grid

    def _setGrid(self, session=None):
        doNothing()

    def _getVehicles(self, session=None):
        return self._vehicles

    def _setVehicles(self, session=None):
        doNothing()

    def _getRides(self, session=None):
        return self._rides

    def _setRides(self, session=None):
        doNothing()

    def _getBonus(self, session=None):
        return self._bonus

    def _setBonus(self, session=None):
        doNothing()

    def _getSteps(self, session=None):
        return self._steps

    def _setSteps(self, session=None):
        doNothing()

    grid = property(_getGrid, _setGrid)
    vehicles = property(_getVehicles, _setVehicles)
    rides = property(_getRides, _setRides)
    bonus = property(_getBonus, _setBonus)
    steps = property(_getSteps, _setSteps)




    def schedule(self):
        print("scheduling")


class Grid:

    _rows,_cols = 0,0

    def __init__(self, rows, cols):  #
        self._rows = rows
        self._cols = cols

    def _getRow(self, session=None):
        return self._rows

    def _setRow(self, session=None):
        doNothing()


    def _getCol(self, session=None):
        return self._cols

    def _setCol(self, session=None):
        doNothing()



    rows = property(_getRow, _setRow)
    cols = property(_getCol, _setCol)


class Ride:
    _startRow, _startCol, _endRow, _endCol, _start, _end = 0,0,0,0,0,0

    def __init__(self, startRow, startCol, endRow, endCol, start, end):
        self._startRow = startRow
        self._startCol =startCol
        self._endRow =endRow
        self._endCol =endCol
        self._start = start
        self._end = end


    def printRide(self):
        print("start Row : " + self.startRow + " start Col : "+ self.startCol + " end row : "+ self.endRow + " end Col : "+ self.endCol + " start time : "+ self.startTime + " end time : "+ self.endTime)


    def _getStartRow(self, session=None):
        return self._startRow


    def _setStartRow(self, session=None):
        doNothing()


    def _getStartCol(self, session=None):
        return self._startCol


    def _setStartCol(self, session=None):
        doNothing()

    def _getEndRow(self, session=None):
     return self._endRow

    def _setEndCol(self, session=None):
        doNothing()

    def _getEndCol(self, session=None):
        return self._endCol

    def _setEndRow(self, session=None):
        doNothing()

    def _getStartTime(self, session=None):
        return self._start

    def _setStartTime(self, session=None):
        doNothing()

    def _getEndTime(self, session=None):
        return self._end

    def _setEndTime(self, session=None):
        doNothing()

    startRow = property(_getStartRow, _setStartRow)
    startCol = property(_getStartCol, _setStartCol)
    endRow = property(_getEndRow, _setEndRow)
    endCol = property(_getEndCol, _setEndCol )
    startTime = property(_getStartTime , _setStartTime )
    endTime = property(_getEndTime, _setEndTime)


def first_line(filedata):
    lines = filedata.split("\n")
    return (lines[0].split(" "))

def createRideObjs(filedata):
    lines = filedata.split("\n")
    rides = []
    b = True
    for x in lines:
        if b:
            b = False
            continue

        xs = x.split(" ")
        if len(x) == 0:
            break

        rides.append(Ride(xs[0], xs[1], xs[2], xs[3], xs[4], xs[5]))
    return rides



        #with open("schedule.txt", 'w') as tarfile:
    #    for line in filedata:
    #        tarfile.write(line)






def doNothing():
    return



if __name__ == "__main__":
   main()
