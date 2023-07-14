import sys
from typing import Optional
from PySide6 import QtGui,QtWidgets,QtCore
from PySide6.QtCore import QSettings
import PySide6.QtWidgets
from ui_splash_screen import Ui_SplashScreen
from ui_GETSTARTED import *
#from ui_interface import *

settings=QSettings()
# global variables
counter=0

# mainwindow
class MainWindow1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################    
        self.setWindowFlags(Qt.FramelessWindowHint) 

        #######################################################################
        ## # Set main background to transparent
        ########################################################################  
        self.setAttribute(Qt.WA_TranslucentBackground)
    
        #######################################################################
        ## # Shadow effect style
        ########################################################################  
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        #######################################################################
        ## # Appy shadow to central widget
        ########################################################################  
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #######################################################################
        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        #######################################################################
        self.setWindowIcon(QIcon(":/icons/icons/github.svg"))
        # Set window tittle
        self.setWindowTitle("MODERN UI")

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        QSizeGrip(self.ui.size_grip)

        #######################################################################
        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())


        #######################################################################
        #Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())


        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################


        #######################################################################
        #Left Menu toggle button
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        window1=MainWindow1()




########################################################################
# Slide left menu function
########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slide_menu_container.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QIcon(u":/icons/icons/align-left.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    #######################################################################





    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################
    #######################################################################



    #######################################################################
    # Update restore button icon on msximizing or minimizing window
    #######################################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(QIcon(u":/icons/icons/minimize-2.svg"))
class loginpage(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.to_login.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.loginpage))
        self.ui.to_register.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Registerpage))
        self.ui.pushButton_4.clicked.connect(self.on_button_clicked)
    def on_button_clicked(self):
        print("Button clicked")
        

# splashscreen
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui= Ui_SplashScreen()
        self.ui.setupUi(self)

        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



        # hide background
        self.ui.background.setMaximumHeight(0)

        # intialize animation
        self.animatelogo()
        self.animate_description()
        self.start_animation()

        # qtimer
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # timer in milliseconds
        self.timer.start(35)

    # animate app logo
    def animatelogo(self):
        opacity_effect=QtWidgets.QGraphicsOpacityEffect(self.ui.logo_img)
        self.ui.logo_img.setGraphicsEffect(opacity_effect)

        self.logo_opacity_animation=QtCore.QPropertyAnimation(
            opacity_effect, b'opacity',duration=1500,startValue=0,endValue=1
        )
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

    # animate app description
    def animate_description(self):
        opacity_effect=QtWidgets.QGraphicsOpacityEffect(self.ui.background)
        self.ui.background.setGraphicsEffect(opacity_effect)

        geometry_animation=QtCore.QPropertyAnimation(
            self.ui.background,b'maximumHeight', duration=1000,startValue=0,endValue=228
        )
        geometry_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        opacity_animation=QtCore.QPropertyAnimation(
            opacity_effect, b'opacity',duration=500,startValue=0,endValue=1
        )
        self.animate_description=QtCore.QParallelAnimationGroup(self.ui.background)
        self.animate_description.addAnimation(geometry_animation)
        self.animate_description.addAnimation(opacity_animation)

    # start animation
    def start_animation(self):
        self.animgroup=QtCore.QSequentialAnimationGroup(self)
        self.animgroup.addAnimation(self.logo_opacity_animation)
        self.animgroup.addAnimation(self.animate_description)
        self.animgroup.start()

    # progress
    def progress(self):
        global counter

        # set the value to prgress bar
        self.ui.progressbar.setValue(counter)
        self.ui.percentage.setText(f"{int(counter)}%")

        # stop the timer
        if counter>100:
            self.timer.stop()

            # show main window
            self.main=loginpage()
            self.main.show()

            # close SplashScreen
            self.close() 
        
        counter+=0.5 
        

if __name__=="__main__":
    app=QtWidgets.QApplication([])
    window=SplashScreen()
    window.show()
    sys.exit(app.exec())
