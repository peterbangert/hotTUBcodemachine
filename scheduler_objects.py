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

        self._grid = Grid(int(x[0]),int(x[1]))
        self._vehicles= int(x[2])
        self.vehicle_list = [Vehicle() for _ in range(self._vehicles)]
        self._rideamount = int(x[3])
        self._bonus = int(x[4])
        self._steps = int(x[5])
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


    @staticmethod
    def dist(x0,y0,x1,y1):
        return abs(x1-x0)+abs(y1-y0)

    def find_optimal_car(self,ride):
        opt_car = None
        opt_val = float('inf')
        ride_length = self.dist(ride.startRow,ride.startCol,ride.endRow,ride.endCol)
        for car in self.vehicle_list:
            pos1 = car.cur_pos
            pos2 = ride.startRow,ride.startCol
            if car.turn_num+self.dist(pos1[0],pos1[1],pos2[0],pos2[1])<ride.endTime-ride_length: #car can make it
                if car.turn_num+self.dist(pos1[0],pos1[1],pos2[0],pos2[1])<ride.startTime:
                    bonus=self._bonus
                else:
                    bonus =0
                if car.turn_num+self.dist(pos1[0],pos1[1],pos2[0],pos2[1])-bonus < opt_val:
                    opt_val = car.turn_num+self.dist(pos1[0],pos1[1],pos2[0],pos2[1])-bonus
                    opt_car = car

        return opt_car, car.turn_num+self.dist(pos1[0],pos1[1],pos2[0],pos2[1])

    def schedule(self):
        self._rides = sorted(self._rides,key=lambda r:r.endTime)

        for ride in self._rides:
            ride_length = self.dist(ride.startRow, ride.startCol, ride.endRow, ride.endCol)
            opt_car, arr_time = self.find_optimal_car(ride)
            opt_car.rides.append(ride)
            opt_car.cur_pos = (ride.endRow,ride.endCol)
            opt_car.turn_num = max(arr_time,ride.startTime) + ride_length


class Vehicle():
    def __init__(self, cur_pos_x=0, cur_pos_y=0, turn_num=0):
        self.cur_pos = cur_pos_x, cur_pos_y
        self.turn_num = turn_num
        self.rides = []


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
        self._startRow = int(startRow)
        self._startCol =int(startCol)
        self._endRow =int(endRow)
        self._endCol =int(endCol)
        self._start = int(start)
        self._end = int(end)


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

