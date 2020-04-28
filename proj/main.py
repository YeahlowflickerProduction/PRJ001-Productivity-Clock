from PySide2 import QtCore as qtc, QtWidgets as qtw, QtGui as qtgui, QtQml as qtqml


class Main(qtc.QObject):

    engine = None
    timer = None
    period = 0
    elapsed = 0
    soundOn = True

    sig_updateTime = qtc.Signal(str)



    #   Initialization
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        engine.rootContext().setContextProperty("manager", self)

        self.sig_updateTime.connect(self.engine.rootObjects()[0].updateTime)

        self.timer = qtc.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.setTimerType(qtc.Qt.TimerType.VeryCoarseTimer)
        self.timer.timeout.connect(self.onTick)




    #   Set period from HH:MM:SS input
    @qtc.Slot(str)
    def setPeriod(self, input):
        self.period = int(input[:2]) * 3600 + int(input[3:5]) * 60 + int(input[6:9])
        self.elapsed = 0




    #   Start/Stop button handler
    @qtc.Slot(bool)
    def toggleTimer(self, isStart):
        if isStart:
            self.timer.start()
        else:
            self.timer.stop()




    #   Returns period in HH:MM:SS
    @qtc.Slot(result=str)
    def getPeriod(self):
        return str(self.secondsToHMS(self.period))





    #   Timer tick handler
    def onTick(self):
        self.elapsed += 1


        #   Check if countdown is completed
        if self.elapsed > self.period:

            #   Play sound when soundOn and countdown is completed
            if self.soundOn:
                from os import system
                system("aplay /mnt/Data/Projects/PRJ001-Productivity-Clock/proj/notify_sound.wav&")

            self.elapsed = 0

        self.sig_updateTime.emit(self.secondsToHMS(self.period - self.elapsed))






    #   Convert seconds to HH:MM:SS
    def secondsToHMS(self, input):
        h = input // 3600
        m = (input - (h * 3600)) // 60
        s = (input - (h * 3600) - (m * 60))
        return "{:02}".format(h) + ":" + "{:02}".format(m) + ":" + "{:02}".format(s)





    #   Update soundOn value
    #   Called by QML button onClicked
    @qtc.Slot(bool)
    def toggleSound(self, val):
        self.soundOn = val