import json
from pprint import pprint
import sys, getopt
import os
import collections
import scheduler_objects


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
            scheduler = scheduler_objects.Scheduler(filedata)
            schedulers.append(scheduler)

    firstScheduler = schedulers[0]
    print(firstScheduler.grid.rows)
    print(firstScheduler.grid.cols)
    for x in firstScheduler.rides:
        x.printRide()
        print(x.startTime)
        print(x.endTime)
        print(x.endTime)

    print(firstScheduler.vehicles)
    print(firstScheduler.bonus)
    print(firstScheduler.steps)


"""
	Session class handles all Session API applications
"""

def wrong_filetype(name) :
    extension = name[name.index("."):]
    filetypes = [".in"]
    if extension in filetypes:
        return False
    return True


if __name__ == "__main__":
   main()
