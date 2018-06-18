'''
Higher Dimensional Visualization Tool created by Kristen Bean June 15, 2018

A tool that allows for data to be visualized as it changes in dimensions beyond 3D. "Frames" are constructed
that allow for the user to select up three dimensional vectors, a label and a viewing range.

'''

import csv
import matplotlib.pyplot as plt

vectors = []
frames = []
events = []

##Write welcome to the program

def loadData():
    filename = input("Location of csv file to pull data from?\n")
        
    with open(filename, 'r') as rawdata:
        reader = csv.reader(rawdata, delimiter=',')
        i = 0
        for row in reader:
            vectors.append(row)

def appHelp():
    ##help interface to the documentation
    pass

def status():
    ##Check the status of vectors, frames and events
    print(len(vectors), " vectors found.")
    counter = 1
    for i in vectors:
        print(counter, "\t", i[0:3])
    print(len(frames), " frames found.")
    for i in frames:
        print(i)

def createFrame():
    '''
    Creates a new frame.
    Frame structure [int number of plots, [plot 1 desig],.., [plot n desig]]
    Plot structure  [x vector, y vector, z vector, x label, y label, z label, xmax, xmin, ymax, ymin, zmax, zmin]
    '''
    newframe = []
    
    queryVectors = input("Vectors for new frame (i.e. \"x, [y], [z]\"):\n")
    tempVectors = queryVectors.split()
    for i in tempVectors:
        newframe.insert(len(newframe), i)
    queryCustom = input("Do you wish to customize the frame?")
    if queryCustom == "yes":
        newframe = customizeFrame(newframe)
    elif queryCustom == "no":
        if len(newframe) == 1:
            newframe.append(10)
            newframe.append(-10)
        elif len(newframe) == 2:
            i=0
            while i < 2:
                newframe.append(10)
                newframe.append(-10)
                i+=1
        elif len(newframe) == 3:
            i=0
            while i < 3:
                newframe.append(10)
                newframe.append(-10)
                i+=1
        else:
            pass
            ##WRITE EXCEPTION FOR GREATER THAN 3 AND IF ANSWER NOT YES/NO
    else:
        pass
    frames.append(newframe)

def customizeFrame(currFrame):
    ##Used to customize a frame
    pass

def deleteFrame():
    ##Deletes an existing frame
    frameSelect = input("Frame to delete?")
    frame = int(frameSelect)-1
    del frames[frame]
    print("Succesfully deleted frame ", frame)

def createEvent():
    ##Creates a new event
    pass

def deleteEvent():
    ##deletes an existing event
    pass

def runEvent():
    ##Runs an event
    pass

def plotFrame():
    ##plots a static frame
    queryFrame = input("Frame to plot: ")
    qF = int(queryFrame)-1
    ##if 1 vector, plot(), if 2 vectors subplot(), if 3 vectors matplot3d()
    frame = frames[qF]
    if len(frame) <= 6:
        plt.plot(frame[0], frame[1])
        plt.subplot(211)
        plt.xlim([frame[3], frame[2]])
        plt.ylim([frame[5], frame[4]])
        plt.show()
    else:
        pass

def interface():
        comm = input(">>>")
        if comm == "load data":
            loadData()
            interface()
        elif comm == "status":
            status()
            interface()
        elif comm == "help":
            appHelp()
            interface()
        elif comm == "create frame":
            createFrame()
            interface()
        elif comm == "create event":
            createEvent()
            interface()
        elif comm == "delete event":
            deleteEvent()
            interface()
        elif comm == "delete frame":
            deleteFrame()
            interface()
        elif comm == "run event":
            runEvent()
            interface()
        elif comm == "plot frame":
            plotFrame()
            interface()
        elif comm == "quit":
            print("Quitting program... \n")
        else:
            print("Command not understood, type 'help' for documentation")
            interface()

interface()
