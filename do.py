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

    arg = str(sys.argv[1])

    if arg is None:
        print("no argument given, exiting")
        sys.exit()
    elif arg == "e":
        print("editing")
        edit()
    elif arg == "c":
        print("counting")
        print("TOTAL WORDS TRANSLATED BY PETER:")
        print(count_words(os.getcwd(), 0, []))
        print("-------------------------------")
    elif arg == "d":
        print("duplicating")
        dir_walker(os.getcwd() )
    elif arg == "s":
        print("searching")
        search_string(os.getcwd() )
    elif arg == "m":
        print("moving")
        move()
    elif arg == "r":
        print("replacing")
        replace()
    else:
        print_helper()

    print("great success")


def dir_walker(path):   #searches given path for file, walks backwards when unsuccessful

    
        for root, dirs, files in os.walk(path):
            for name in files:
                #print root
                copy_rename(os.path.join(root, name))
            

        
def copy_rename(name) :
    if (wrong_filetype(name)) :
        return

    bashcmd = "cp " + name + " " + adjusted_filename(name)
    print(bashcmd)
    os.system(bashcmd)
    

    return 0

def adjusted_filename(name):
    suffix = input("Add suffix to copied file? : ")
    return "'" +name[0: name.index(".")] + suffix + name[name.index("."):] +"'" 

def wrong_filetype(name) :
    extension = name[name.index("."):]
    filetypes = [".md", ".txt", ".text", ".doc", ".docx"]
    if extension in filetypes:
        return False
    return True
    

def edit():
    yn = input("Standard googletranslate file edit ? (y/n) : ")
    if (yn.lower() == "y"):
        find_replace()
        return

    yn = input(".text to .md reformat ? (y/n) : ")
    if (yn.lower() == "y"):
        txt_to_md()
        return

    print("said no to all options, do nothing.")


def txt_to_md():
    searchText = ["h1(top).","h1.", "bc.", "p.", "h2(top).","h2.", "@", "|"]
    replaceText = ["# ", "## ", "~~~\n", "", "### ", "## ", "`", "\n|---|---|\n"]

    path = os.getcwd() 
    for root, dirs, files in os.walk(path):
        #if root != path:
        #    break
        print(files)
        for file in files:
            if file.endswith(".text") or  file.endswith(".txt"):
                with open(os.path.join(root, file), 'r') as tarfile :
                    filedata = tarfile.read()
                    print(file)

                    # Replace the target string
                for i in range(len(searchText)):

                    if (searchText[i] == "bc." or searchText[i] == "|"):
                        if (searchText[i] not in filedata):
                            continue
                        replace = filedata[filedata.index(searchText[i]):]
                        print(replace)
                        replace = replace[: replace.index("\n\n")]
                        print(replace)
                        if (searchText[i] == "bc."):
                            filedata = filedata.replace(replace, replace + "\n" + replaceText[i] )
                            filedata = filedata.replace(searchText[i], replaceText[i])
                        else :
                            filedata = filedata.replace(replace, replaceText[i] + replace)

                    else:
                        filedata = filedata.replace(searchText[i], replaceText[i])

                    print(searchText[i] + replaceText[i])

                newfile = os.path.join(root, file[0:file.index(".")]+".md")
                bashcmd = "cp " + "'"+ os.path.join(root, file) +"'"+ " " + "'"+newfile+"'"
                print(bashcmd)
                os.system(bashcmd)

                    # Write the file out again
                with open(newfile, 'w') as tarfile:
                    tarfile.write(filedata)




def ggt_to_md():
    searchText = [" [", "] ", " / ", "/ i", "& Nbsp;"," # "," @", "@ "]
    replaceText = ["[","]","/","/i","&nbsp;", "#", "@","@" ]

    path = os.getcwd() 
    for root, dirs, files in os.walk(path):
        if root != path:
            break
        print(files)
        for file in files:
            if "(EN_US)" in file:

                with open(file, 'r') as tarfile :
                    filedata = tarfile.read()
                    print(file)

                    # Replace the target string
                for i in range(len(searchText)):
                    filedata = filedata.replace(searchText[i], replaceText[i])
                    print(searchText[i] + replaceText[i])

                    # Write the file out again
                with open(file, 'w') as tarfile:
                    tarfile.write(filedata)


def count_words(path, words, visited):
    mustContain = input("What must filename conatin? : ")
    for root, dirs, files in os.walk(path):
        
        for file in files:
            if mustContain in file:
                print(file)
                #visited.append(file)
                with open(os.path.join(root,file)) as fh:
                    words += len(fh.read().split())
            
    thefile = open('test.txt', 'w')    
    return words      


def search_string(path):

    args = input("what search for plz? : ").split(",")
    print(args)
    for root, dirs, files in os.walk(path):
        for name in files:
            searchable = args


            try:
                file_string_finder(root, name, searchable)
            except IOError as e:
                str = e
                #print "I/O error({0}): {1} could not open {2} ".format(e.errno, e.strerror, str(root)+str(name))
            except ValueError:
                print("Could not convert data to an integer.")
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise


            if any(srch in name.lower() for srch in searchable):
                results_printer(root, name, " ")

        
def file_string_finder(root, filename, target):
    response = "  "
    with open(os.path.join(root, filename)) as f:
        contents = f.read().lower()
        for x in target:
            count = contents.count(x)
            if count != 0:
                response += (" {0}({1})".format(x, str(count)))

    if response != "  ":
        results_printer(root, filename, response)


def results_printer(root, name, result):
    print(os.path.join(root, name)) + result

def move():
    filename = input("filename plz, with extension : ")
    dest = input("destination plz, just folder name : ")
    filePath = find(filename, os.getcwd())
    print("moving file : " + filePath)
    possibleDestinations = []
    for root, dirs, files in os.walk(os.getcwd()):
        for dirnames in dirs:
            if dirnames == dest:
                possibleDestinations.append(os.path.join(root, dirnames))
    x =1
    print("-------------------------")
    print("Possible Destinations : ")
    for dest in possibleDestinations:
        print(str(x) + ". " + dest)
        x+=1

    selecting = True
    while(selecting) :

        selection = int(input("please select one : "))
        if selection > len(possibleDestinations) or selection < 1 :
            print("Did not enter a correct number, please try again")
        else:
            selecting = False

    print("to destination : " + possibleDestinations[selection - 1])
    bashcmd = "mv " + filePath + " " + possibleDestinations[selection-1]
    os.system(bashcmd)



def find(name, path):   #searches given path for file, walks backwards when unsuccessful

    looking = True
    while (looking):

        for root, dirs, files in os.walk(path):
            if name in files:
                looking = False
                return os.path.join(root, name)

        path = os.path.normpath(os.getcwd() + os.sep + os.pardir)


def replace():
    while (True):
        searchText = input("Text to Replace : ")
        replaceText = input("Replace with : ")

        path = os.getcwd() 
        for root, dirs, files in os.walk(path):
            if root != path:
                break
            print(files)
            for file in files:
                with open(file, 'r') as tarfile :
                    filedata = tarfile.read()
                    print(file)

                    # Replace the target string
                for i in range(len(searchText)):
                    filedata = filedata.replace(searchText, replaceText)

                    # Write the file out again
                with open(file, 'w') as tarfile:
                    tarfile.write(filedata)

        again = input("again? (y/n) : ")
        if (again.lower() != "y"):
            break



def print_helper():
    print ( "HELP ----   " 
        + "\n" + "There are a couple single character arguments that can be given"
        + "\n" + "---------------------------------------------------------------" 
        + "\n" + "e : edit"
        + "\n" + "     -> this will edit all english files for pescy mistranslations. only in CWD!"
        + "\n" + "" 
        + "\n" + "c : counting"
        + "\n" + "     -> this argument will count all of the words of every english file"
        + "\n" + ""
        + "\n" + "d : duplicating"
        + "\n" + "     -> This argument will copy every file and add the (EN_US) suffix to it."
        + "\n" + ""
        + "\n" + "m : moving"
        + "\n" + "     -> This argument will prompt you for an input file and a destination folder."
        + "\n" + ""
        + "\n" + "s : search"
        + "\n" + "     -> This argument will prompt you for input (CSV) in which to search for."
        + "\n" + ""
        + "\n" + "r : replace"
        + "\n" + "     -> This argument will replace all files in CWD with replacement string."
        + "\n" 
    )

if __name__ == "__main__":
   main()
