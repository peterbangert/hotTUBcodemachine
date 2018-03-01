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


def main():

    filesincwd =[]
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        if root != path:
            break
        print(files)
        for file in files:
            if wrong_filetype(file) :
                continue

            filesincwd.append(file)
    schedulers = []

    for file in filesincwd:
        with open(file, 'r') as tarfile:
            filedata = tarfile.read()
            print(file)
            scheduler = Scheduler(filedata)
            schedulers.append(scheduler)

    firstScheduler = schedulers[0]
    print(firstScheduler.grid.rows)
    print(firstScheduler.grid.cols)
    print(firstScheduler.rides)
    print(firstScheduler.vehicles)


"""
	Session class handles all Session API applications
"""


class Scheduler:
    _grid, _vehicles, _rideamount = "", "", ""
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
        self._grid = session

    def _getVehicles(self, session=None):
        return self._vehicles

    def _setVehicles(self, session=None):
        self._vehicles = session

    def _getRides(self, session=None):
        return self._rides

    def _setRides(self, session=None):
        self._rides = session

    grid = property(_getGrid, _setGrid)
    vehicles = property(_getVehicles, _setVehicles)
    rides = property(_getRides, _setRides)



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
        self._rows = session


    def _getCol(self, session=None):
        return self._cols

    def _setCol(self, session=None):
        self._cols = session



    rows = property(_getRow, _setRow)
    cols = property(_getCol, _setCol)


class Ride:

    def __init__(self, startRow, startCol, endRow, endCol, start, end):
        self.startRow = startRow
        self.startCol =startCol
        self.endRow =endRow
        self.endCol =endCol
        self.startTime = start
        self.endTime = end



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




def wrong_filetype(name) :
    extension = name[name.index("."):]
    filetypes = [".in"]
    if extension in filetypes:
        return False
    return True


def pretty_printer(dict):

    "{:<20} {:<20}".format('About', 'Information')
    for k, v in dict.iteritems():
        if v == "":
            continue
        if isinstance(v, list):
            print
            "{:<20} {:<20}".format(k, ', '.join(v))
            continue

        print
        "{:<20} {:<20}".format(k, v)




if __name__ == "__main__":
   main()
