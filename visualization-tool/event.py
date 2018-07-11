from visualizationtool import vectors

def createEvent():
    event = []
    print("Here are the current vectors loaded into the program:")
    i = 1
    for v in vectors:
        print(i, "\t", v[1:5])
        i+=1
    return(event)


