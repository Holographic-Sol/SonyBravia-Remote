import sys
import subprocess
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0

tvTurnOnThread = ()
tvTurnOffThread = ()
tvSelectThread = ()
tvCursorUpThread = ()
tvCursorDownThread = ()
tvCursorLeftThread = ()
tvCursorRightThread = ()
tvHomeThread = ()
tvOptionsThread = ()
tvReturnThread = ()
tvGuideThread = ()
tvVolumeUpThread = ()
tvVolumeDownThread = ()
tvVolumeMuteThread = ()
tvChannelUpThread = ()
tvChannelDownThread = ()
tvPlayThread = ()
tvPauseThread = ()
tvPreviousThread = ()
tvSkipThread = ()
tvStopThread = ()
tvExitThread = ()

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.title = "Sony Bravia WiFi Remote"
        self.left = 760
        self.top = 0
        self.width = 400
        self.height = 135
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.initUI()

    def initUI(self):
        global tvTurnOnThread
        global tvTurnOffThread
        global tvSelectThread
        global tvCursorUpThread
        global tvCursorDownThread
        global tvCursorLeftThread
        global tvCursorRightThread
        global tvHomeThread
        global tvOptionsThread
        global tvReturnThread
        global tvGuideThread
        global tvVolumeUpThread
        global tvVolumeDownThread
        global tvVolumeMuteThread
        global tvChannelUpThread
        global tvChannelDownThread
        global tvPlayThread
        global tvPauseThread
        global tvPreviousThread
        global tvSkipThread
        global tvStopThread
        global tvExitThread
        global tvDisplayThread
        global tvInputThread
        global tvPopUpMenuThread
        global tvFastForwardThread
        global tvReverseThread
        global tvSENThread

        self.setWindowTitle('Sony Bravia WiFi Remote')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("./Resources/Sony-Entertainment-Network-Small_48x48.ico"))

        def tvTurnOnFunction():
            tvTurnOnThread.start()
        def tvTurnOffFunction():
            tvTurnOffThread.start()
        def tvSelectFunction():
            tvSelectThread.start()
        def tvCursorUpFunction():
            tvCursorUpThread.start()
        def tvCursorDownFunction():
            tvCursorDownThread.start()
        def tvCursorLeftFunction():
            tvCursorLeftThread.start()
        def tvCursorRightFunction():
            tvCursorRightThread.start()
        def tvHomeFunction():
            tvHomeThread.start()
        def tvOptionsFunction():
            tvOptionsThread.start()
        def tvReturnFunction():
            tvReturnThread.start()
        def tvGuideFunction():
            tvGuideThread.start()
        def tvVolumeUpFunction():
            tvVolumeUpThread.start()
        def tvVolumeDownFunction():
            tvVolumeDownThread.start()
        def tvVolumeMuteFunction():
            tvVolumeMuteThread.start()
        def tvChannelUpFunction():
            tvChannelUpThread.start()
        def tvChannelDownFunction():
            tvChannelDownThread.start()
        def tvPlayFunction():
            tvPlayThread.start()
        def tvPauseFunction():
            tvPauseThread.start()
        def tvPreviousFunction():
            tvPreviousThread.start()
        def tvSkipFunction():
            tvSkipThread.start()
        def tvStopFunction():
            tvStopThread.start()
        def tvExitFunction():
            tvExitThread.start()
        def tvDisplayFunction():
            tvDisplayThread.start()
        def tvInputFunction():
            tvInputThread.start()
        def tvPopUpMenuFunction():
            tvPopUpMenuThread.start()
        def tvFastForwardFunction():
            tvFastForwardThread.start()
        def tvReverseFunction():
            tvReverseThread.start()
        def tvSENFunction():
            tvSENThread.start()

        tvOnButton = QPushButton(self)
        tvOnButton.move(60, 0)
        tvOnButton.resize(25, 25)
        tvOnButton.clicked.connect(tvTurnOnFunction)
        tvOnButton.setIcon(QIcon("./Resources/power.png"))
        tvOnButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvOffButton = QPushButton(self)
        tvOffButton.move(310, 0)
        tvOffButton.resize(25, 25)
        tvOffButton.clicked.connect(tvTurnOffFunction)
        tvOffButton.setIcon(QIcon("./Resources/poweroff.png"))
        tvOffButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvSelectButton = QPushButton(self)
        tvSelectButton.move(180, 55)
        tvSelectButton.resize(40, 40)
        tvSelectButton.clicked.connect(tvSelectFunction)
        tvSelectButton.setIcon(QIcon("./Resources/select.png"))
        tvSelectButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvCursorUpButton = QPushButton(self)
        tvCursorUpButton.move(180, 15)
        tvCursorUpButton.resize(40, 40)
        tvCursorUpButton.clicked.connect(tvCursorUpFunction)
        tvCursorUpButton.setIcon(QIcon("./Resources/cursor_up.png"))
        tvCursorUpButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvCursorDownButton = QPushButton(self)
        tvCursorDownButton.move(180, 95)
        tvCursorDownButton.resize(40, 40)
        tvCursorDownButton.clicked.connect(tvCursorDownFunction)
        tvCursorDownButton.setIcon(QIcon("./Resources/cursor_down.png"))
        tvCursorDownButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvCursorLeftButton = QPushButton(self)
        tvCursorLeftButton.move(140, 55)
        tvCursorLeftButton.resize(40, 40)
        tvCursorLeftButton.clicked.connect(tvCursorLeftFunction)
        tvCursorLeftButton.setIcon(QIcon("./Resources/cursor_left.png"))
        tvCursorLeftButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvCursorRightButton = QPushButton(self)
        tvCursorRightButton.move(220, 55)
        tvCursorRightButton.resize(40, 40)
        tvCursorRightButton.clicked.connect(tvCursorRightFunction)
        tvCursorRightButton.setIcon(QIcon("./Resources/cursor_right.png"))
        tvCursorRightButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvHomeButton = QPushButton(self)
        tvHomeButton.move(115, 25)
        tvHomeButton.resize(25, 25)
        tvHomeButton.clicked.connect(tvHomeFunction)
        tvHomeButton.setIcon(QIcon("./Resources/home.png"))
        tvHomeButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvOptionsButton = QPushButton(self)
        tvOptionsButton.move(125, 0)
        tvOptionsButton.resize(40, 20)
        tvOptionsButton.clicked.connect(tvOptionsFunction)
        tvOptionsButton.setText('Options')
        tvOptionsButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvReturnButton = QPushButton(self)
        tvReturnButton.move(150, 100)
        tvReturnButton.resize(25, 25)
        tvReturnButton.clicked.connect(tvReturnFunction)
        tvReturnButton.setIcon(QIcon("./Resources/return.png"))
        tvReturnButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvGuideButton = QPushButton(self)
        tvGuideButton.move(275, 0)
        tvGuideButton.resize(30, 20)
        tvGuideButton.clicked.connect(tvGuideFunction)
        tvGuideButton.setText('Guide')
        tvGuideButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvVolumeUpButton = QPushButton(self)
        tvVolumeUpButton.move(60, 35)
        tvVolumeUpButton.resize(30, 20)
        tvVolumeUpButton.clicked.connect(tvVolumeUpFunction)
        tvVolumeUpButton.setText('VOL+')
        tvVolumeUpButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvVolumeDownButton = QPushButton(self)
        tvVolumeDownButton.move(60, 95)
        tvVolumeDownButton.resize(30, 20)
        tvVolumeDownButton.clicked.connect(tvVolumeDownFunction)
        tvVolumeDownButton.setText('VOL-')
        tvVolumeDownButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvVolumeMuteButton = QPushButton(self)
        tvVolumeMuteButton.move(60, 65)
        tvVolumeMuteButton.resize(30, 20)
        tvVolumeMuteButton.clicked.connect(tvVolumeUpFunction)
        tvVolumeMuteButton.setText('Mute')
        tvVolumeMuteButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvChannelUpButton = QPushButton(self)
        tvChannelUpButton.move(310, 35)
        tvChannelUpButton.resize(25, 20)
        tvChannelUpButton.clicked.connect(tvChannelUpFunction)
        tvChannelUpButton.setText('CH+')
        tvChannelUpButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvChannelDownButton = QPushButton(self)
        tvChannelDownButton.move(310, 95)
        tvChannelDownButton.resize(25, 20)
        tvChannelDownButton.clicked.connect(tvChannelDownFunction)
        tvChannelDownButton.setText('CH-')
        tvChannelDownButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvPlayButton = QPushButton(self)
        tvPlayButton.move(150, 25)
        tvPlayButton.resize(25, 25)
        tvPlayButton.clicked.connect(tvPlayFunction)
        tvPlayButton.setIcon(QIcon("./Resources/media-play.png"))
        tvPlayButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvPauseButton = QPushButton(self)
        tvPauseButton.move(225, 25)
        tvPauseButton.resize(25, 25)
        tvPauseButton.clicked.connect(tvPauseFunction)
        tvPauseButton.setIcon(QIcon("./Resources/media-pause.png"))
        tvPauseButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvPreviousButton = QPushButton(self)
        tvPreviousButton.move(90, 65)
        tvPreviousButton.resize(25, 25)
        tvPreviousButton.clicked.connect(tvPreviousFunction)
        tvPreviousButton.setIcon(QIcon("./Resources/media-previous.png"))
        tvPreviousButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvSkipButton = QPushButton(self)
        tvSkipButton.move(285, 65)
        tvSkipButton.resize(25, 25)
        tvSkipButton.clicked.connect(tvSkipFunction)
        tvSkipButton.setIcon(QIcon("./Resources/media-skip.png"))
        tvSkipButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvStopButton = QPushButton(self)
        tvStopButton.move(225, 100)
        tvStopButton.resize(25, 25)
        tvStopButton.clicked.connect(tvStopFunction)
        tvStopButton.setIcon(QIcon("./Resources/media-stop.png"))
        tvStopButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvExitButton = QPushButton(self)
        tvExitButton.move(245, 0)
        tvExitButton.resize(25, 20)
        tvExitButton.clicked.connect(tvExitFunction)
        tvExitButton.setText('Exit')
        tvExitButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvDisplayButton = QPushButton(self)
        tvDisplayButton.move(205, 0)
        tvDisplayButton.resize(40, 20)
        tvDisplayButton.clicked.connect(tvDisplayFunction)
        tvDisplayButton.setText('Display')
        tvDisplayButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvInputButton = QPushButton(self)
        tvInputButton.move(170, 0)
        tvInputButton.resize(30, 20)
        tvInputButton.clicked.connect(tvInputFunction)
        tvInputButton.setText('Input')
        tvInputButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvPopUpMenuButton = QPushButton(self)
        tvPopUpMenuButton.move(260, 25)
        tvPopUpMenuButton.resize(25, 25)
        tvPopUpMenuButton.clicked.connect(tvPopUpMenuFunction)
        tvPopUpMenuButton.setIcon(QIcon("./Resources/pop-up-menu.png"))
        tvPopUpMenuButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvReverseButton = QPushButton(self)
        tvReverseButton.move(120, 65)
        tvReverseButton.resize(25, 25)
        tvReverseButton.clicked.connect(tvReverseFunction)
        tvReverseButton.setIcon(QIcon("./Resources/media-reverse.png"))
        tvReverseButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvFastForwardButton = QPushButton(self)
        tvFastForwardButton.move(255, 65)
        tvFastForwardButton.resize(25, 25)
        tvFastForwardButton.clicked.connect(tvFastForwardFunction)
        tvFastForwardButton.setIcon(QIcon("./Resources/media-ff.png"))
        tvFastForwardButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: green;
           border:1px solid rgb(0, 0, 0);}"""
        )
        tvSENButton = QPushButton(self)
        tvSENButton.move(90, 0)
        tvSENButton.resize(30, 20)
        tvSENButton.clicked.connect(tvSENFunction)
        tvSENButton.setText('Apps')
        tvSENButton.setStyleSheet(
            """QPushButton {background-color: rgb(0, 0, 0);
           color: rgb(0, 80, 255);
           border:1px solid rgb(0, 0, 0);}"""
        )

        tvTurnOnThread = tvTurnOnClass()
        tvTurnOffThread = tvTurnOffClass()
        tvSelectThread = tvSelectClass()
        tvCursorUpThread = tvCursorUpClass()
        tvCursorDownThread = tvCursorDownClass()
        tvCursorLeftThread = tvCursorLeftClass()
        tvCursorRightThread = tvCursorRightClass()
        tvHomeThread = tvHomeClass()
        tvOptionsThread = tvOptionsClass()
        tvReturnThread = tvReturnClass()
        tvGuideThread = tvGuideClass()
        tvVolumeUpThread = tvVolumeUpClass()
        tvVolumeDownThread = tvVolumeDownClass()
        tvVolumeMuteThread = tvVolumeMuteClass()
        tvChannelUpThread = tvChannelUpClass()
        tvChannelDownThread = tvChannelDownClass()
        tvPlayThread = tvPlayClass()
        tvPauseThread = tvPauseClass()
        tvPreviousThread = tvPreviousClass()
        tvSkipThread = tvSkipClass()
        tvStopThread = tvStopClass()
        tvExitThread = tvExitClass()
        tvDisplayThread = tvDisplayClass()
        tvInputThread = tvInputClass()
        tvPopUpMenuThread = tvPopUpMenuClass()
        tvFastForwardThread = tvFastForwardClass()
        tvReverseThread = tvReverseClass()
        tvSENThread = tvSENClass()

        self.show()

class tvTurnOnClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvTurnOnClass. Thread Connected...')
        cmd = ('python ' + 'tvturnon.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvTurnOffClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvTurnOffClass. Thread Connected...')
        cmd = ('python ' + 'tvturnoff.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvSelectClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvSelectClass. Thread Connected...')
        cmd = ('python ' + 'tvselect_enter.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvCursorUpClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvCursorUpClass. Thread Connected...')
        cmd = ('python ' + 'tvcursorup1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvCursorDownClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvCursorDownClass. Thread Connected...')
        cmd = ('python ' + 'tvcursordown1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvCursorLeftClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvCursorLeftClass. Thread Connected...')
        cmd = ('python ' + 'tvcursorleft1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvCursorRightClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvCursorRightClass. Thread Connected...')
        cmd = ('python ' + 'tvcursorright1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvHomeClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvHoemClass. Thread Connected...')
        cmd = ('python ' + 'tvhome.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvOptionsClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvOptionsClass. Thread Connected...')
        cmd = ('python ' + 'tvoptions.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvReturnClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvReturnClass. Thread Connected...')
        cmd = ('python ' + 'tvreturn.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvGuideClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvGuideClass. Thread Connected...')
        cmd = ('python ' + 'tvguide.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvVolumeUpClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvVolumeUpClass. Thread Connected...')
        cmd = ('python ' + 'tvvolumeup1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvVolumeDownClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvVolumeDownClass. Thread Connected...')
        cmd = ('python ' + 'tvvolumedown1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvVolumeMuteClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvVolumeMuteClass. Thread Connected...')
        cmd = ('python ' + 'tvmute.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvChannelUpClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvChannelUpClass. Thread Connected...')
        cmd = ('python ' + 'tvchannelup1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvChannelDownClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvChannelDownClass. Thread Connected...')
        cmd = ('python ' + 'tvchanneldown1.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvPlayClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvPlayClass. Thread Connected...')
        cmd = ('python ' + 'tvplay.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvPauseClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvPauseClass. Thread Connected...')
        cmd = ('python ' + 'tvpause.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvPreviousClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvPreviousClass. Thread Connected...')
        cmd = ('python ' + 'tvprevious.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvSkipClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvSkipClass. Thread Connected...')
        cmd = ('python ' + 'tvnext.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvStopClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvStopClass. Thread Connected...')
        cmd = ('python ' + 'tvstop.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvExitClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvExitClass. Thread Connected...')
        cmd = ('python ' + 'tvexit.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvDisplayClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvDisplayClass. Thread Connected...')
        cmd = ('python ' + 'tvdisplay.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvInputClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvInputClass. Thread Connected...')
        cmd = ('python ' + 'tvinput.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvPopUpMenuClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvPopUpMenuClass. Thread Connected...')
        cmd = ('python ' + 'tvpopUpMenu.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvFastForwardClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvFastForwardClass. Thread Connected...')
        cmd = ('python ' + 'tvforward.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvReverseClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvReverseClass. Thread Connected...')
        cmd = ('python ' + 'tvreverse.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

class tvSENClass(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __def__(self):
        self.wait()
    def run(self):
        print('plugged in: tvSENClass. Thread Connected...')
        cmd = ('python ' + 'tvsonyEntertainmentNetwork.py')
        subprocess.Popen(cmd, shell=False, startupinfo=info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
