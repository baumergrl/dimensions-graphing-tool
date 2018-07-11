

def plotFrame():
    ##plots a static frame
    queryFrame = input("Frame to plot: ")
    qF = int(queryFrame)-1
    ##if 1 vector, plot(), if 2 vectors subplot(), if 3 vectors matplot3d()
    frame = frames[qF]
    if len(frame) <= 6:
        plt.plot(frame[0], frame[1])
        plt.xlim([frame[3], frame[2]])
        plt.ylim([frame[5], frame[4]])
        plt.show()
    else:
        pass
